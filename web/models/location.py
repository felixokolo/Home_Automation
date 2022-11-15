#!/usr/bin/python3
"""
Model for Node locations
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import web.models.base as base
from web.models.base import BaseModel
from web.models.engine.dbStorage import Storage

class Location(BaseModel, base.Base):
    """
    Location class for nodes

    ...
    Attributes
    ----------
    __table__ : string
        Name of table
    name : str
        Obeject ID

    """
    name = Column(String(50), nullable=False)

    __tablename__ = 'locations'

    def __init__(self, id, name, *args, **kwargs):
        """
        Init method for Location class
        Args:
        name  : Integer
            Node ID
        """
        if type(name) is not str:
            raise Exception("Name must be a string")
        super().__init__(id, *args, **kwargs)
        self.name = name
        base.Base.metadata.create_all(Storage.engine)
        Storage.session.add(self)
        Storage.session.commit()


