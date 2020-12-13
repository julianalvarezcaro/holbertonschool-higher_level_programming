#!/usr/bin/python3
"""City class module
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """City class
    """
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
