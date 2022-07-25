import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

print(dfCrime[(dfCrime['Primary Type'] == 'HOMICIDE') & (dfCrime['Location Description'] == 'STREET')].count()['ID'])
