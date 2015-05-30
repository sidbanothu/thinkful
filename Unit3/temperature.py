# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:48:03 2015

@author: sidba_000
"""

#b3d63e6828bdf7067803e9682207342a
#https://api.forecast.io/forecast/b3d63e6828bdf7067803e9682207342a/LATITUDE,LONGITUDE 
#https://api.forecast.io/forecast/b3d63e6828bdf7067803e9682207342a/LATITUDE,LONGITUDE,TIME 

import requests
import sqlite3 as lite
import datetime

#cities dictionary with lat & long
cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }
        
api_key = "b3d63e6828bdf7067803e9682207342a"
url = "https://api.forecast.io/forecast/" + api_key

## create a databse with columns (date, city1 .. city 5) to hold the max temperature for the day
con = lite.connect("weather.db")
cur = con.cursor()

city_keys = cities.keys()
city_columns = [ str(x) + ' INT' for x in city_keys]

with con:
    cur.execute ("DROP TABLE IF EXISTS daily_temp")
    cur.execute ("CREATE TABLE daily_temp (date_reading REAL, " + ",".join(city_columns) + ")")

end_date = datetime.datetime.date(datetime.datetime.now())
query_date = end_date - datetime.timedelta(days =30)


## insert date values into the table
with con:
    while query_date <= end_date:
######!!!!!!!        cur.execute("INSERT INTO daily_temp (date_reading) VALUES (?)", str(query_date) )
        cur.execute("INSERT INTO daily_temp (date_reading) VALUES (?)", ((query_date),))

        query_date += datetime.timedelta(days =1)

#### Testing
import pandas as pd
with con:
    cur.execute("SELECT * FROM daily_temp")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

print df
#### Testing Complete

### Now load the database by making calls to API
for k, v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days =30)
    while query_date <= end_date:
        url2 = url + "/" + v + "," + query_date.strftime('%Y-%m-%dT%H:%M:%S')
        r = requests.get(url2)
        max_temp = r.json()['daily']['data'][0]['temperatureMax']
        with con:
            query = "UPDATE daily_temp SET " + k + "="+ str(max_temp) + " WHERE date_reading = " + "'" + str(query_date) + "'"
            print query
            cur.execute(query)
        query_date += datetime.timedelta(days =1)

#### Testing
import pandas as pd 
with con:
    cur.execute("SELECT * FROM daily_temp")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df1 = pd.DataFrame(rows, columns=cols)

print df1
#### Testing Complete

import collections

date_change = collections.defaultdict(int)
incr_temp_change = collections.defaultdict(int)
dec_temp_change = collections.defaultdict(int)

for col in df1.columns:
    if col != 'date_reading':
        col_values = df1[col].tolist()
        print len(col_values)
        for i in range(len(col_values)-1):
            change = int(col_values[i+1]) - int(col_values[i])
            if change > incr_temp_change[col]: 
                incr_temp_change[str(col)]= change
            if change < incr_temp_change[col]: 
                dec_temp_change[str(col)]= change
### ANSWER!!
for k in incr_temp_change:
    print "Most Temperature increase in" + k + " was " + str(incr_temp_change[k])
    
for k in incr_temp_change:
    print "Most Temperature decrease in" + k + " was " + str(dec_temp_change[k])
    
df1.plot(x=df1['date_reading'])
