import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

print(dfCrime[dfCrime['Domestic'] == 1].groupby('Primary Type', as_index=False).size().sort_values('size').iloc[-1])
