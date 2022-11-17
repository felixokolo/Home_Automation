#!/usr/bin/python3
"""
Model for Node locations
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from web.models.base import Base
from web.models.base import BaseModel
from web.models.node import Node


import web.models as models
from uuid import uuid4

class Location(BaseModel, Base):
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
    light_nodes = relationship("Node")

    def __init__(self, name, *args, **kwargs):
        """
        Init method for Location class
        Args:
        name  : string
            Location name
        """

        ids = str(uuid4())
        super().__init__(ids, name, *args, **kwargs)
        models.storage.new(self)
