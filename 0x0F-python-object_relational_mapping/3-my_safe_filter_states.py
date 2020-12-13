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
    name = args[4]

    db = MySQLdb.connect(host='127.0.0.1',
                         port=3306,
                         user=username,
                         db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()