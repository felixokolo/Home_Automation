#!/usr/bin/python3
"""
Model for Node locations
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
import web.models.base as base
from web.models.base import BaseModel
from web.models.engine.dbStorage import Storage
from uuid import uuid4

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

    __tablename__ = 'locations'
    light_nodes = relationship("Light")

    def __init__(self, name, *args, **kwargs):
        """
        Init method for Location class
        Args:
        name  : Integer
            Node ID
        """

        id = str(uuid4())
        super().__init__(id, name *args, **kwargs)
        base.Base.metadata.create_all(Storage.engine)
        Storage.session.add(self)
        Storage.session.commit()
