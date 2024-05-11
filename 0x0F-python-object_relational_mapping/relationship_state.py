#!/usr/bin/python3
"""Contains the class definition of a State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """Class representing a state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
