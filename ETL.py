# Libraries needed for the tutorial

import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account

url1 = "https://github.com/nytimes/covid-19-data/raw/master/us.csv" # Make sure the url is the raw version of the file on GitHub
newyork = requests.get(url1).content
url2 = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1597037488088r0.13033000065342848"
recovery = requests.get(url2).content
# Reading the downloaded content and turning it into a pandas dataframe

df1 = pd.read_csv(io.StringIO(newyork.decode('utf-8')))
df2 = pd.read_csv(io.StringIO(recovery.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print (df1.head())
print (df2.head())

