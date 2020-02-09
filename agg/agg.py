import json
import logging
import os
import re

import yaml

from utils import get_page_html as _get_page_html

logging.basicConfig()
logger = logging.getLogger('DataHerb.Metadata.Aggregator.App')

__cwd__ = os.getcwd()
__location__ = os.path.realpath(
    os.path.join(__cwd__, os.path.dirname(__file__))
)
_FLORA_BASE_FOLDER = "flora"
_FLORA_TRANSFORMED_FOLDER = "build"

logger.debug(
    f"__cwd__ is {__cwd__}"
)
logger.debug(
    f"__location__ is {__location__}"
)


def flora_metadata_files():
    """
    fetch_flora_metadata loads all the flora metadata files
    """
    flora_files = os.listdir(
        os.path.join(__location__, '..', _FLORA_BASE_FOLDER)
    )
    flora_files = [i for i in flora_files if i.endswith(".yml")]

    logger.info(f"Total number of flora: {len(flora_files)}")

    return flora_files


def flora_metadata(flora_files):
    """
    load_flora_metadata loads the metadata files into a dictionary

    :param flora_files: list of flora files locally
    :type flora_files: list
    :return: all metadata about the herbs in flora
    :rtype: dict
    """

    logger.debug("BEGIN: retrieve flora metadata")
    re_herb_name = re.compile(r"(.+?)(\.[^.]*$|$)")

    flora_meta = {}
    for herb_name in flora_files:
        with open(os.path.join(__location__, '..', _FLORA_BASE_FOLDER, herb_name)) as fp:
            try:
                herb = yaml.load(fp, Loader=yaml.FullLoader)
                herb = herb[0]
                flora_meta[re_herb_name.findall(herb_name)[0][0]] = herb
                logger.debug(herb)
            except Exception as e:
                logger.warn(f"{herb_name} can not be loaded! \n{e}")
                pass

    logger.debug("END: retrieve flora metadata")

    return flora_meta


def load_herb_metadata(herb_name, flora_herb_meta, container, herbs_to_fix=None):
    """
    load_herb_metadata loads the metadata of the herb using the specific repository in flora

    :param herb_name: metadata file name of the herb in flora
    :param herb_name: str
    :param flora_herb_meta: a single herb metadata entry in flora
    :type flora_herb_meta: dict
    :param container: dictionary to be updated to store the herb metadata
    :type container: dict
    """

    logger.debug("BEGIN: retrieve flora metadata")

    herb_repository = flora_herb_meta.get("repository")
    herb_repository_meta_link = f"https://raw.githubusercontent.com/{herb_repository}/master/dataset/metadata.yml"

    herb_repository_meta_response = _get_page_html(herb_repository_meta_link)
    if herb_repository_meta_response.get("status") == 200:
        try:
            herb_repository_meta = yaml.load(
                herb_repository_meta_response.get("page").content, Loader=yaml.FullLoader
            )
            herb_repository_meta = herb_repository_meta[0]
        except:
            pass
        # merge flora metadata and herbs metadata
        flora_herb_meta = {
            **flora_herb_meta,
            **herb_repository_meta
        }
        # assign the metadata to the herb name
        container[herb_name] = flora_herb_meta

    elif herb_repository_meta_response.get("status") == 404:
        if herbs_to_fix is not None:
            herbs_to_fix.append(herb_name)
        else:
            logger.warning(f"Could not find metadata for {herb_name} in specific repository {herb_repository}")

    logger.debug("END: retrieve flora metadata")


def main():

    flora_files = flora_metadata_files()
    flora_meta = flora_metadata(flora_files)
    herbs_to_fix = []
    flora = {}
    for herb_name, herb_meta in flora_meta.items():
        load_herb_metadata(herb_name, herb_meta, flora, herbs_to_fix)

    with open(
        os.path.join(__location__, '..', _FLORA_TRANSFORMED_FOLDER, 'flora.json'),
        'w'
    ) as fp:
        json.dump(
            {
                "flora": flora,
                "herbs_to_fix": herbs_to_fix,
                "total_herbs": len(flora)
            }, fp
        )



if __name__ == "__main__":
    main()
    logger.debug("End of Game")
