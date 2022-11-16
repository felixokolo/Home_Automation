#!/usr/bin/python3
"""
Model of schedules
"""

from models.base import Base
from models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
import web.models.base as base
from web.models.base import BaseModel
from web.models.engine.dbStorage import Storage
from uuid import uuid4

node_schedules =Table(  "node_schedules",
                        Base.metadata,
                        Column("light_id", ForeignKey("lights.id"), primary_key=True),
                        Column("schedule_id", ForeignKey("schedules.id"), primary_key=True),)

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



    action_time = Column(String, nullable=False)
    action = Column(String, nullable=False)
    action_node = relationship("Light", secondary=node_schedules)
    id = str(uuid4())

    def __init__(self, name, *args, **kwargs):
        """
        Init for schedules
        """
        super(id, name, *args, **kwargs)
