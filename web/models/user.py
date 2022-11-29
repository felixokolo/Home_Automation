#!/usr/bin/python3
"""
Model of schedules
"""

from web.models.base import Base
from web.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from uuid import uuid4
import web.models as models
from web.models.location import Location
from web.models.node import Node

class User(BaseModel, Base):
    """
    User class for user records

    ...
    Attributes
    ----------
    __tablename__ : string
        Name of table
    username : string
        Username of user

    """

    __tablename__ = "users"
    username = Column(String(50), primary_key=True, unique=True)
    nodes = relationship("Location")

    def __init__(self, uname, name, *args, **kwargs):
        """
        Init for users

        Args:
        uname : string
            Username of user
        """
        __ids = str(uuid4())

        if (models.storage.psession.
            query(self.__class__.username).
            filter_by(username=uname).first() is not None):
            print("username exists")
            raise Exception("Username already exists")

        super().__init__(__ids, name, *args, **kwargs)
        self.username = uname
        models.storage.new(self)

    @classmethod
    def get_locs(cls, uname):
        """
        Get all locations associted to a user

        Args:
            uname : String
                username to search
        """

        users = models.storage.get_class(cls.__name__);
        locs = models.storage.get_class("Location");
        ret = []
        if users is None:
            return None
        for user in users:
            if user.username == uname:
                ret = [loc for loc in locs if loc.user_id == user.id]
                return ret
