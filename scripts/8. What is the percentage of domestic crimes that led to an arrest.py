import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

tmp_df = dfCrime[dfCrime['Domestic'] == 1]
print(tmp_df['Arrest'].sum() / tmp_df['Arrest'].size)
