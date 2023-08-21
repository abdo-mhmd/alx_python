#!/usr/bin/python3
"""lists all State objects from the database 'hbtn_0e_6_usa'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:4306/{}"
                           .format(sys.argv[1],sys.argv[2],sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(State.id, State.name))

    session.close()