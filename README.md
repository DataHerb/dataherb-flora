# dataherb-flora

<h1 align="center">
  <br>
  <a href="https://dataherb.github.io"><img src="https://raw.githubusercontent.com/DataHerb/dataherb.github.io/master/assets/favicon/ms-icon-310x310.png" alt="Markdownify" width="200"></a>
  <br>
  DataHerb Flora
  <br>
</h1>

<h4 align="center">A <a href="https://dataherb.github.io" target="_blank">DataHerb</a> Core Service to Bundle the Datasets into Flora.</h4>

<p align="center">
    <img src="https://github.com/DataHerb/dataherb-flora/workflows/CI%20Update%20Jekyll/badge.svg?branch=master">
</p>

## What is DataHerb

DataHerb is an open data initiative to make the access of open datasets easier.

- A **DataHerb** or **Herb** is a dataset. A dataset comes with the data files, and the metadata of the data files.
- A **DataHerb Leaf** or **Leaf** is a data file in the DataHerb.
- A **Flora** is the combination of all the DataHerbs.

In many data projects, finding the right datasets to enhance your data is one of the most time consuming part. DataHerb adds flavor to your data project.

## What is DataHerb Flora

We desigined the following workflow to share and index datasets.

![DataHerb Workflow](https://raw.githubusercontent.com/DataHerb/dataherb.github.io/master/assets/images/dataherb-components.png)

This repository is being used for listing of datasets (Listings in DataHerb flora repository).

## How to Add Your Dataset

> [A Complete **Tutorals**](https://dataherb.github.io/add/)

Simply create a `yml` file in the `flora` folder to link to your dataset repository. Your dataset repository should have a `.dataherb` folder and a `metadata.yml` file in it.

The indexing part will be done by [GitHub Actions](https://github.com/DataHerb/dataherb-flora/actions).

## How is Everything Connected

There are three components to build the dataset index.

1. [dataherb-flora](https://github.com/DataHerb/dataherb-flora): Index datasets using yml files.
2. [dataherb-metadata-aggregator](https://github.com/DataHerb/dataherb-metadata-aggregator): Aggregrates all information about the datasets and create database.
3. [dataherb.github.io](https://github.com/DataHerb/dataherb.github.io): Builds the website using the database.

Some packages are also created to make the access and creation of the datasets easier. Refer to [the website](https://dataherb.github.io/) for the details.
