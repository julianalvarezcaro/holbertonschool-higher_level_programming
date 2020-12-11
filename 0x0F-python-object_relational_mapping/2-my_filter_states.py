#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
Arguments received:
    MySQL username, MySQL password, database name
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    u = args[1]
    # p = args[2]
    n = args[3]
    name = args[4]

    db = MySQLdb.connect(host='127.0.0.1', port=3306, user=u, db=n)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name =\
'{}' ORDER BY states.id".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
