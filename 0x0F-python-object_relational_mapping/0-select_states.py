#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
Arguments received:
    MySQL username, MySQL password, database name
"""

import MySQLdb
import sys


if __name__ == "__main__":

    args = sys.argv
    username = args[1]
    password = args[2]
    db_name = args[3]

    db = MySQLdb.connect(host='127.0.0.1',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
