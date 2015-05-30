# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:27:04 2015

@author: sidba_000
"""

import requests
r = requests.get('http://www.citibikenyc.com/stations/json')
print r.json().keys()
print r.json()['executionTime']
#print r.json()['stationBeanList']
print len (r.json()['stationBeanList'])

key_list = [] # unique key for each station

# stationBeanList is a list which has some keys
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
                key_list.append(k)

print key_list

print r.json()['stationBeanList'][0]['id']


from pandas.io.json import json_normalize
df = json_normalize(r.json()['stationBeanList'])

print df.head()

import matplotlib.pyplot as plt
import pandas as pd

#df['availableBikes'].hist()
#plt.show()

print df['totalDocks'].mean()

condition = (df['statusValue'] == 'In Service')
condition2 = (df['availableBikes'] == 24)
print df[( df['statusValue'] == 'In Service') & (df['availableBikes'] == 12)].head()

import sqlite3 as lite
con = lite.connect('citi_bike2.db')
cur = con.cursor()

with con:
    cur.execute('DROP TABLE IF EXISTS citibike_reference' )
    cur.execute(''' 
    CREATE TABLE citibike_reference (
        id INT PRIMARY KEY,
        totalDocks INT,
        city TEXT,
        altitude INT, 
        stAddress2 TEXT,
        longitude NUMERIC,
        postalCode TEXT,
        testStation TEXT,
        stAddress1 TEXT,
        stationName TEXT,
        landMark TEXT,
        latitude NUMERIC,
        location TEXT
        )
    ''')
    
sql = '''
INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, 
longitude, postalCode, testStation, stAddress1, stationName, landMark, 
latitude, location) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
'''


#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))
        
station_ids= df['id'].tolist()
print station_ids

station_ids = ['_' + str(x) + 'INT' for x in station_ids]
print station_ids[0]

with con:
    cur.execute('DROP TABLE IF EXISTS available_bikes' )
    cur.execute(" CREATE TABLE available_bikes ( execution_time INT, " + ", ".join(station_ids) + ")" )

with con:
    cur.execute("SELECT * FROM available_bikes")
    rows = cur.fetchall()
    for row in cur.fetchall():
        print(row)


import time

from dateutil.parser import parse
import collections

exec_time = parse(r.json()['executionTime'])
print exec_time

with con:
    cur.execute( 'INSERT INTO available_bikes (execution_time) VALUES(?)', (exec_time.strftime('%Y-%m-%dT%H:%M:%S'),))

id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

#loop through the stations in the station list
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

#iterate through the defaultdict to update the values in the database
with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%Y-%m-%dT%H:%M:%S') + ";")        
    
    
    
    



