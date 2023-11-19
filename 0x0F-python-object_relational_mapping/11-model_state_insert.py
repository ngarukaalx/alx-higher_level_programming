#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import collate

if __name__ == "__main__":
    """to check if the script is being run directly not imported
    """
    usaername, password, db_name = sys.argv[1:4]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(usaername, password,  db_name),  pool_pre_ping=True
            )

    session = sessionmaker(bind=engine)

    session = session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    new_added = session.query(State).filter(
            State.name == 'Louisiana').first()

    if new_added:
        print("{}".format(new_added.id))

    session.close()
