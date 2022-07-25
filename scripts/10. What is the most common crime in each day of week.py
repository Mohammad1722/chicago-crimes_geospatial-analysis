import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

dfCrime['dayofweek'] = (dfCrime['Date'].dt.dayofweek+1)%7 # get day of week and make it start from sunday
tmp = dfCrime.groupby(by=['dayofweek', 'Primary Type'], as_index=False).size()
print(tmp[tmp.groupby('dayofweek')['size'].rank('dense', ascending=False) == 1])
