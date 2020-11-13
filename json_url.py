import pandas as pd
import os
import teradata
import datetime
import io
import requests
import json

today = datetime.datetime.today()
yesterday = today.day-1
year = today.year
month = today.month

url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json'
site = requests.get(url)
data = site.text
list_data = json.loads(data)
data = list_data['features']
data = [i["attributes"] for i in data]
dataset = pd.DataFrame(data,columns=['OBJECTID', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths'])
del dataset['Last_Update']
del dataset['OBJECTID']
dataset['Confirmed'] = dataset['Confirmed'].fillna(0)
dataset['Recovered'] = dataset['Recovered'].fillna(0)
dataset['Deaths'] = dataset['Deaths'].fillna(0)
dataset['BuildDate'] = today.strftime("%c")
dataset = dataset.loc[dataset['Country_Region'] == 'US']
