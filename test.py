import pandas as pd

url1 = "https://github.com/nytimes/covid-19-data/raw/master/us.csv"
df1 = pd.read_csv(url1)
#print(df1.head())

url2 = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1597037488088r0.13033000065342848"
cols_list2= ["Recovered"]
df2 = pd.read_csv(url2)
#df1.columns =[column.replace("/", "_") for column in df1.columns]
#region= df1[df1.Country_Region=="US"].head()
#print(region)
#df2 = pd.concat([region, df[df.date.isin(region.Date)]])
#df2= pd.merge()
df2=df2.drop(["Deaths","Confirmed"], axis=1)
df3=pd.merge(df2, df1, left_on='Date', right_on='date',how='outer')
df3.columns =[column.replace("/", "_") for column in df3.columns]
df4= df3[df3.Country_Region=="US"]
df4=df4.drop(["Province_State","Lat","Long","date"], axis=1)
print(df4.head(20))


df4.to_csv(r'E:\Cloudlight\EDP_AWS\test1.csv', index = False)