#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import relationship
import sys

if __name__ == "__main__":
    """only execute when script is run directly
    """
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, db_name), pool_pre_ping=True
            )

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    session = session()

    state_obj = (
            session.query(City)
            .options(joinedload(City.State))
            .order_by(City.id)
            .all()
            )

    for city in state_obj:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
