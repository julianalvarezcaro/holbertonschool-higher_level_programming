#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
Arguments received:
    MySQL username, MySQL password, database name
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

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

    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
             states ON cities.state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
