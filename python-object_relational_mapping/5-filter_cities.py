#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
   where name matches matches an argument passed as a parameter"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %(state)s"""

    cursor.execute(query, {'state': state})
    result = cursor.fetchall()
    lenght = len(result)

    if lenght == 0:
        print('')
    for i in range(lenght):
        if i < lenght - 1:
            print(result[i][1], end=", ")
        else:
            print(result[i][1])

    cursor.close()
    db.close()
