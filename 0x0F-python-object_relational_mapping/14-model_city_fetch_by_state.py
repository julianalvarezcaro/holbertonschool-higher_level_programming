#!/usr/bin/python3
"""Write a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    quer = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in quer:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
