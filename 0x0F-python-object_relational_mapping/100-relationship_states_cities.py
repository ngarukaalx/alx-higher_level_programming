#!/usr/bin/python3
"""script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """execute only when run directly
    """
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, db_name), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    california = State(name='California', cities=[City(name='San Francisco')])
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(california)
    session.commit()

    session.close()
