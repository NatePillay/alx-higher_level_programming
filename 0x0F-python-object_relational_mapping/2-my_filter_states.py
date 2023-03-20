#!/usr/bin/python3
"""
    script that lists all states matching user input
    from the database hbtn_0e_0_usa
    Usage:
    ./2-my_filter_states.py <mysql username> <mysql password> <database name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` WHERE name LIKE BINARY '{}' \
            ORDER BY `id`".format(argv[4]))
    [print(state) for state in cur.fetchall()]
