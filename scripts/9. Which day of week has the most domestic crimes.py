import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

print(dfCrime[dfCrime['Domestic'] == 1].groupby(dfCrime['Date'].dt.dayofweek).size().sort_values().iloc[-1])
