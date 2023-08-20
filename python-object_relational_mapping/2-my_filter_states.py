#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
   where name matches matches an argument passed as a parameter"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(name)

    cursor.execute(query)

    for row in cursor.fetchall():
        if row[1] == name:
            print(row)

    cursor.close()
    db.close()
