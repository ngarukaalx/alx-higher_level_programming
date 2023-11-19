#!/usr/bin/python3
""" script that changes the name of a State object from
the database hbtn_0e_6_usa
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

    name_update = session.query(State).filter(
            State.id == 2).first()

    if name_update:
        name_update.name = 'Texas'

        session.commit()

    session.close()
