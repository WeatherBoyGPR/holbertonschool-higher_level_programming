#!/usr/bin/python3
""" Will list all State objects from database hbtn_0e_6_usa """

from model_state import Base, State
from sys import argv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    sqlstr = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    sqlstr = sqlstr.format(argv[1], argv[2], argv[3])
    engine = create_engine(sqlstr, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
