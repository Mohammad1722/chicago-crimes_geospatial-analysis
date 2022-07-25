import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

tmp_df = dfCrime[(dfCrime['Primary Type'] == 'HOMICIDE')].groupby('Location Description', as_index=False).size().sort_values(by=['size'], ascending=False).iloc[0:5]
print(tmp_df)