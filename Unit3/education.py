# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:06:53 2015

@author: sidba_000
"""

from bs4 import BeautifulSoup
import requests

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content)
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


for link in soup.find_all('a'):
    print link.get('href')
    
import sqlite3 as lite

con = lite.connect('UNdata.db')
cur= con.cursor()

with con:
    create_query = '''
    CREATE TABLE undata (country_name TEXT, male_school_life_exp INT,
    female_school_life_exp INT, year_analysis TEXT)
    '''
    cur.execute ("DROP TABLE IF EXISTS undata")

    cur.execute(create_query)
