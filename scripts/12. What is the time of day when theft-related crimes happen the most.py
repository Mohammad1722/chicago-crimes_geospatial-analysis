import pandas as pd
import geopandas as gpd

file_name_crime = "./data/chicagoCrimes/Chicago_Crimes_cleaned.pkl"
dfCrime = pd.read_pickle(file_name_crime)
dfCrime = gpd.GeoDataFrame(dfCrime, geometry='g')

dfCrime['hour'] = dfCrime['Date'].dt.hour
theftRelatedList = ["MOTOR VEHICLE THEFT", "BURGLARY", "ROBBERY", "THEFT"]
print(
    dfCrime[
        (dfCrime['Primary Type'] == "MOTOR VEHICLE THEFT") |
        (dfCrime['Primary Type'] == "BURGLARY") |
        (dfCrime['Primary Type'] == "ROBBERY") |
        (dfCrime['Primary Type'] == "THEFT")
    ].groupby('hour', as_index=False).size().sort_values('size').iloc[-1]
)
