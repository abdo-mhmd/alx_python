#!/usr/bin/python3
"""prints the first State object from the database 'hbtn_0e_6_usa'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    
    session = sessionmaker(bind=engine)()
    filter_name = session.query(State).filter(State.name.like('%a%'))
    for state in filter_name:
        print("{}: {}".format(state.id, state.name))
    
    session.close()