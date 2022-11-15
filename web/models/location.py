#!/usr/bin/python3
"""
Model for Node locations
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from web.models.base import BaseModel

class Location(BaseModel, BaseModel.Base):
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

    __table__ = 'locations'
    def __init__(self, name):
        """
        Init method for Location class
        Args:
        name  : Integer
            Node ID
        """
        if type(name) is not str:
            raise Exception("Name must be a string")
        super().__init__
        self.name = name
