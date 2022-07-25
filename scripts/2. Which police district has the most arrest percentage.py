import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

district_group = dfCrime.groupby('District', as_index=True)
print((district_group['Arrest'].sum() / district_group['Arrest'].count()).sort_values(ascending=False).iloc[[0]])