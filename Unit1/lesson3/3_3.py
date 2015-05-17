# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite
import pandas as pd
# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('getting_started.db')

# with con:
#   # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
#   cur = con.cursor()    
#   cur.execute('SELECT SQLITE_VERSION()')
#   # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
#   data = cur.fetchone()
#   # Finally, print the result.
#   print "SQLite version: %s" % data


# Inserting rows by passing values directly to `execute()`
with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("DROP VIEW IF EXISTS Cities_Weather")
    cur.execute("CREATE TABLE cities(state text, city text)")
    cur.execute("CREATE TABLE weather(city text, year text, month text, temperature int)") 
    cur.execute("INSERT INTO cities VALUES('WA', 'seattle')")
    cur.execute("INSERT INTO cities VALUES('WA', 'tacoma')")
    cur.execute("INSERT INTO cities VALUES('WA', 'bellevue')")
    cur.execute("INSERT INTO cities VALUES('OR', 'portland')")
    cur.execute("INSERT INTO cities VALUES('IL', 'chicago')")
    cur.execute("INSERT INTO cities VALUES('IL', 'moline')")
    cur.execute("INSERT INTO cities VALUES('TX', 'houston')")    
    cur.execute("INSERT INTO weather VALUES('houston', 2015, 'July', '100')")
    cur.execute("INSERT INTO weather VALUES('houston', 2015, 'June', '80')")
    cur.execute("INSERT INTO weather VALUES('chicago', 2015, 'July', '70')")
    cur.execute("INSERT INTO weather VALUES('seattle', 2015, 'June', '100')")
    cur.execute("INSERT INTO weather VALUES('seattle', 2015, 'July', '100')")
    cur.execute("INSERT INTO weather VALUES('seattle', 2015, 'Aug', '80')")
    cur.execute("INSERT INTO weather VALUES('tacoma', 2015, 'June', '75')")
    cur.execute("INSERT INTO weather VALUES('tacoma', 2015, 'July', '50')")
    cur.execute("INSERT INTO weather VALUES('tacoma', 2015, 'Aug', '60')")

    # user_input = "empty"
    # while user_input != "":
    #   state = raw_input("Enter state:")
    #   city = raw_input("Enter city:")
    #   year = raw_input("Enter year:")
    #   month = raw_input("Enter month:")
    #   temperature = raw_input("Enter temperature:")
    #   cur.execute("INSERT INTO cities VALUES(?,?)", (state,city))
    #   cur.execute("INSERT INTO weather VALUES(?,?,?,?)", (city, year, month, temperature))

    #   user_input = raw_input("Continue?:")

    cur.execute("CREATE VIEW Cities_Weather AS SELECT state, cities.city, month, temperature FROM cities INNER JOIN weather on cities.city = weather.city")

    cur.execute("SELECT * FROM Cities_Weather")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    print("Joined Data is")
    for row in rows:
        print row

    cur.execute("SELECT state, month, AVG(temperature) FROM Cities_Weather GROUP BY state, month")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    print("Joined Data is")
    for row in rows:
        print row
    cur.execute("SELECT state, month, AVG(temperature) FROM Cities_Weather GROUP BY month")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    print("Joined Data is")
    for row in rows:
        print row
# cities = (('Las Vegas', 'NV'), 
#                     ('Atlanta', 'GA'))

# weather = (('Las Vegas', 2013, 'July', 'December'),
#                      ('Atlanta', 2013, 'July', 'January'))

# # Inserting rows by passing tuples to `execute()`
# with con:

#     cur = con.cursor()
#     cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
#     cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)
