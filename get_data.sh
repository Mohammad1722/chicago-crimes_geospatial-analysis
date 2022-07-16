#!/usr/bin/env bash

mkdir -p data
mkdir -p data/chicagoCrimes
mkdir -p data/zcta5

echo ""; echo ""
echo "------------------------------------------------------------------------"
echo "Downloading the datasets..."
echo "---------------------------"

wget -nc https://star.cs.ucr.edu/datasets/Chicago%20Crimes/download.json.gz -O data/chicagoCrimes/Chicago_Crimes.json.gz
wget -nc https://star.cs.ucr.edu/datasets/TIGER2018/ZCTA5/download.json.gz?mbr=-88.07241,41.62385,-87.14613,42.05043 -O data/zcta5/TIGER2018_ZCTA5.json.gz


echo ""; echo ""
echo "------------------------------------------------------------------------"
echo "Extracting the data..."
echo "----------------------"

yes n | gzip -dkNv data/chicagoCrimes/Chicago_Crimes.json.gz
yes n | gzip -dkNv data/zcta5/TIGER2018_ZCTA5.json.gz

