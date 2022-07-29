# Chicago Crimes Geospatial Analysis

This repository is part of the Google Summer of Code (GSoC) project: "Geospatial Data Analysis with AsterixDB". 

AsterixDB is a parallel big-data management system that is highly scalable. It can manage semi-structured data but also supports a query language with the expressiveness of SQL. It provides a ﬂexible data model that supports modern NoSQL applications with a powerful query processor that can scale to billions of records and terabytes of data.  

The main goals of this project are:
* Understanding how to build a scalable data science project using AsterixDB.
* Translating common questions to SQL queries and running them on large data.
* Comparing AsterixDB with other tools like Pandas.
* Learning how to visualize the results of queries and present them.

## Requirements
Make sure you have downloaded AsterixDB, the datasets, and successfully installed all the packages/libraries in this section.
* Run the script [`get_data.sh`](get_data.sh) to download the datasets
    ```bash
    $ cd path/to/this/repository
    $ ./get_data.sh
    ```
* Make sure you have installed the following python libraries:  
    * [notebook](https://jupyter.org/install#jupyter-notebook)
    * [NumPy](https://numpy.org/)
    * [Matplotlib](https://matplotlib.org/)
    * [pandas](https://pandas.pydata.org/)
    * [GeoPandas](https://geopandas.org/en/stable/)
    * [geoplot](https://residentmario.github.io/geoplot/)
    ```sh
    $ pip3 install numpy matplotlib pandas geopandas notebook
    $ sudo apt install libproj-dev proj-data proj-bin libgeos-dev
    $ pip3 install geoplot
    ```

## Project Contents
* [Notebooks](./notebooks/):  
    1. [Preprocessing.ipynb](./notebooks/Preprocessing.ipynb) contains the preprocessing steps that are used on the datasets before analyzing them in Python.  
    If you want to replicate the results of this project you'll have to execute the cells of this notebook at least once after downloading the datasets to generate the pickle files that are loaded by the 2nd notebook.

    2. [chicago_crimes.ipynb](./notebooks/chicago_crimes.ipynb) contains the proposed questions on the datasets, as well as the AsterixDB queries and the Pandas code used to answer each question.

* [Scripts](./scripts/):  
    This folder contains the Pandas code for each question separately and is used to measure the execution time for each question independently.
    
* [Tutorials](./tutorials/):
    This folder contains tutorials about using AsterixDB for performing Data Analysis using AsterixDB.
    1. [Installing AsterixDB](./tutorials/Installing%20AsterixDB/installing_asterixdb.md)
    2. [Loading the Datasets](./tutorials/Loading%20the%20Datasets/loading_the_datasets.md)
    3. [Simple Data Analysis Questions](./tutorials/Simple%20Data%20Analysis%20Questions/simple_data_analysis_questions.md)

