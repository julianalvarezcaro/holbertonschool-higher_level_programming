#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
Arguments received:
    MySQL username, MySQL password, database name
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()
    cur.close()
