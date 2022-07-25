import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

file_name_zipcode = "./data/zcta5/TIGER2018_ZCTA5.pkl"
dfZipCode = pd.read_pickle(file_name_zipcode)
dfZipCode = gpd.GeoDataFrame(dfZipCode, geometry='g')

tmp = dfCrime.sjoin(dfZipCode, how='inner')
print(tmp.groupby('GEOID10', as_index=False).size().sort_values(by='size', ascending=False).reset_index(drop=True).iloc[:5])