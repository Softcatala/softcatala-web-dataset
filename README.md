# Repository description

This repository contains Sofcatalà web site content (articles and programs descriptions).

Dataset are available in the [dataset](dataset/) directory.

Dataset size:
* articles.json contains 623 articles with 373233 words
* programes.json contains 330 program descripctions with 49868 words

The license of the data is Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

# How to update the dataset

How to update the dataset:
* Export the _programes_ and _articles_ items from WordPress admin interface
* Save the raw files into _/raw _directory
* Run _./filter.sh_ to filter out sensitive data
* Do pip install requirements
* Run _python wp-to-json.py_
