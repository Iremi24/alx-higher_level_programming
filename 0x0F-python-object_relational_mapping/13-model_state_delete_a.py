#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a
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

    # Query to find all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    # Delete all found State objects
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close session
    session.close()
