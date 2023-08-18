#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """
    City class:
    can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
