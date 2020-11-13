import pandas as pd
import os
import teradata
import datetime
import io
import requests

yesterday = today.day-1
year = today.year
month = today.month

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

try:
    site = requests.get(url)
    data = site.text
    data = io.StringIO(data)
    dataset = pd.read_csv(data)
    dataset = dataset.drop(columns=['UID','iso2','iso3','code3','FIPS','Admin2','Lat','Long_','Combined_Key'])
    dataset = dataset.melt(id_vars=['Province_State','Country_Region'], var_name="Date", value_name="Value")
    dataset['Date'] = dataset['Date']+'20'
    dataset['Date'] = pd.to_datetime(dataset['Date'])
    dataset['Value'] = dataset['Value'].fillna(0)
    dataset['BuildDate'] = today.strftime("%c")
    
except requests.exceptions.ConnectionError:
    print('Failed')
