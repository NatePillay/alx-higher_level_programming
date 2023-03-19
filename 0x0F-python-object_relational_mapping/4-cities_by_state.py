#!/usr/bin/python3
""" 
Display all values for city in DB hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
                 FROM cities JOIN states ON cities.state_id = states.id
                 ORDER BY cities.id ASC""")
    [print(city) for city in c.fetchall()]
