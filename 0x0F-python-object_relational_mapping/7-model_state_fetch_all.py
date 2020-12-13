#!/usr/bin/python3

"""Write a script that lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    username = args[1]
    password = args[2]
    db_name = args[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).all()
    for instance in query:
        print("{}: {}".format(instance.id, instance.name))
    session.close()
