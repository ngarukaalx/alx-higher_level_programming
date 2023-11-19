#!/usr/bin/python3
"""script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import collate

if __name__ == "__main__":
    """to check if the script is being run directly not imported
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
            )

    session = sessionmaker(bind=engine)

    session = session()

    states_a = session.query(State).filter(
            collate(State.name, 'utf8mb4_bin').like(
                '%a%')).order_by(State.id).all()

    for state in states_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
