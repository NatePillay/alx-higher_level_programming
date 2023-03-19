#!/usr/bin/python3
"""
   script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE '{:s}' ORDER BY cities.id ASC".format(argv[4]))
    [print(city) for city in c.fetchall()]
