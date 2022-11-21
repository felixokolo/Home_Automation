#!/usr/bin/python3
"""
Model for Node locations
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from web.models.base import Base
from web.models.base import BaseModel
from web.models.node import Node
#from web.models.user import User


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
    user_id = Column(String(50), ForeignKey("users.id"))
    light_nodes = relationship("Node")

    def __init__(self, name, user_id, *args, **kwargs):
        """
        Init method for Location class
        Args:
        name  : string
            Location name
        """

        ids = str(uuid4())
        super().__init__(ids, name, *args, **kwargs)
        self.user_id = user_id
        models.storage.new(self)

    @classmethod
    def get_nodes(cls, loc_id):
        """
        Get all nodes associted to a Location

        Args:
            loc_id : String
                Location id to search
        """

        locs = models.storage.get_class(cls.__name__);
        if locs is None:
            return None
        for loc in locs:
            if loc.id == loc_id:
                nodes = Node.get_loc_nodes(loc.id)
                return nodes
