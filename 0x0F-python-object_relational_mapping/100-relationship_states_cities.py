#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco”"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name="California")

    # Create new City object
    new_city = City(name="San Francisco", state=new_state)

    # Add objects to session
    session.add(new_state)
    session.add(new_city)

    # Commit changes
    session.commit()

    # Print the new city ID
    print(new_city.id)

    # Close session
    session.close()
