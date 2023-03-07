#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# model "Dog" has name and breed attributes
class Dog(Base):
    __tablename__ = 'dogs'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    id = Column(Integer())
    name = Column(String())
    breed = Column(String())

    


