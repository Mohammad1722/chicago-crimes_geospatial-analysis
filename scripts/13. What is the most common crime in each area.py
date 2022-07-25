import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

file_name_zipcode = "./data/zcta5/TIGER2018_ZCTA5.pkl"
dfZipCode = pd.read_pickle(file_name_zipcode)
dfZipCode = gpd.GeoDataFrame(dfZipCode, geometry='g')

joint_df = dfCrime.sjoin(dfZipCode, how='inner')
tmp = joint_df.groupby(by=['GEOID10', 'Primary Type'], as_index=False).size()
print(tmp[tmp.groupby('GEOID10')['size'].rank('first', ascending=False) == 1])
