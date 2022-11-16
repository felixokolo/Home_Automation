#!/usr/bin/python3

"""
Model of general nodes
"""
from models.base import Base
from models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import web.models.base as base
from web.models.base import BaseModel
from web.models.engine.dbStorage import Storage
from web.models.schedule import node_schedules


class Light(BaseModel, Base):
    """
    Location class for nodes

    ...
    Attributes
    ----------
    __tablename__ : string
        Name of table
    status : string
        Status of node ON or OFF
    brihtness : float
        Brightness level in percentage 0 - 100 %
    schedules : list
        List of ON or OFF schedules

    """

    __tablenme__ = 'lights'
    brightnes = Column(Float)
    location_id = Column(String, ForeignKey("locations.id"))
    schedules = relationship("Schedule", secondary=node_schedules)

    def __init__(self, id, name, *args, **kwargs):
        """
        Init method for light nodes
        """

        super().__init__(id, name, *args, **kwargs)
