#!/usr/bin/python3
"""
Model of schedules
"""

from web.models.base import Base
from web.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
import web.models.base as base
from web.models.base import BaseModel
from web.models import storage
from uuid import uuid4
from datetime import datetime

class Schedule(BaseModel, Base):
    """
    Schedule class for schedule actions

    ...
    Attributes
    ----------
    __tablename__ : string
        Name of table
    action_time : DateTime
        Action execution time
    action : string
        required action

    """

    __tablename__ = "schedules"



    action_time = Column(String(50), nullable=False)
    action = Column(String(50), nullable=False)
    # lights = relationship( "Light",
    #                             secondary=node_schedules,
    #                             back_populates="schedules")
    ids = str(uuid4())

    def __init__(self, name, a_time, action, *args, **kwargs):
        """
        Init for schedules
        """
        super().__init__(self.ids, name, *args, **kwargs)
        self.action_time = datetime.strptime(a_time, "%Y/%m/%d %H:%M:%S:%f")
        self.action = action
        storage.new(self)
