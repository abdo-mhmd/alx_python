#!/usr/bin/python3
"""lists all states from the database 'hbtn_0e_0_usa'"""

import MySQLdb as s
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = s.connect(host="localhost", port=3306,
                       user=username, passwd=password, db=database)
    except s.Error as e:
        print(e)

    cur = db.cursor()
    cur.execute("SELECT * FROM {}.states ORDER BY states.id".format(database))

    for data in cur.fetchall():
        print(data)

    cur.close()
    db.close()
