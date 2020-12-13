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

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    cur = db.cursor()

    cur.execute(
        "SELECT GROUP_CONCAT(DISTINCT cities.name SEPARATOR ', ')\
        FROM cities\
        JOIN states ON cities.state_id=states.id\
        WHERE states.name=%s", (name,))

    for row in cur:
        print(row[0])

    cur.close()
    db.close()
