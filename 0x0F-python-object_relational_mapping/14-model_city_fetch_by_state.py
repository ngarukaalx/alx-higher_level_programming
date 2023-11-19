#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    cities_obj = (
            session.query(State.name, City.id, City.name)
            .filter(State.id == City.state_id)
            .order_by(City.id)
            .all()
            )

    for entries in cities_obj:
        state_name, city_id, city_name = entries

        print(f"{state_name}: ", end="")
        print(f"({city_id}) {city_name}")

    session.close()
