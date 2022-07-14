# Chicago Crimes Geospatial Analysis

This repository is part of Google Summer of Code (GSoC) project: "Geospatial Data Analysis with AsterixDB".  

## Requirements
* Run the script [`get_data.sh`](get_data.sh) to download the datasets
    ```bash
    cd path/to/this/repository
    ./get_data.sh
    ```
* Make sure you have installed the following python libraries:  
    * [NumPy](https://numpy.org/)
    * [Matplotlib](https://matplotlib.org/)
    * [pandas](https://pandas.pydata.org/)
    * [GeoPandas](https://geopandas.org/en/stable/)
    * [geoplot](https://residentmario.github.io/geoplot/)
    * [notebook](https://jupyter.org/install#jupyter-notebook)
    ```sh
    pip3 install numpy matplotlib pandas geopandas geoplot notebook
    ```
## **Important Note**
The [geoplot](https://residentmario.github.io/geoplot/) library has many dependencies with specific compatible verseions that you may need to install manyally in order to get the library to work. A [`conda`](https://www.anaconda.com/) environment may solve this issue but I haven't tested it yet.  
Everything in this repository is developed on `Ubuntu 22.04` with `Python 3.10.4`.