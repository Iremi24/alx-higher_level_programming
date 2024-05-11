#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new State object to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close session
    session.close()
