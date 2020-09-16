import pandas as pd

url1 = "https://github.com/nytimes/covid-19-data/raw/master/us.csv"
cols_list= ["date"]
df = pd.read_csv(url1, usecols= cols_list)
#print(df.head())

url2 = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1597037488088r0.13033000065342848"
cols_list2= ["Recovered"]
df1 = pd.read_csv(url2)
df1.columns =[column.replace("/", "_") for column in df1.columns]
region= df1[df1.Country_Region=="US"].head()
#print(region)



df2 = pd.concat([region, df[df.date.isin(region.Date)]])
print(df2)