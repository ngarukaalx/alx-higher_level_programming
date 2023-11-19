#!/usr/bin/python3
"""script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    """only execute when script is run directly
    """
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name), pool_pre_ping=True
            )

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    session = session()

    state_obj = (
            session.query(State)
            .options(joinedload(State.cities))
            .order_by(State.id)
            .all()
            )

    for state in state_obj:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
