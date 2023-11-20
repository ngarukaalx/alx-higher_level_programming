#!/usr/bin/python3
""" script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import collate

if __name__ == "__main__":
    """to check if the script is being run directly not imported
    """
    usaername, password, db_name, state_search = sys.argv[1:5]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(usaername, password,  db_name),  pool_pre_ping=True
            )

    session = sessionmaker(bind=engine)

    session = session()

    state_obj = session.query(State).filter(
            State.name == state_search).first()

    if state_obj:
        print("{}".format(state_obj.id))
    else:
        print("Not found")

    session.close()
