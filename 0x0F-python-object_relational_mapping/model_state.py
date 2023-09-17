#!/usr/bin/python3
""" State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"
