#!/usr/bin/python3

"""
Model of general nodes
"""
from web.models.base import Base
from web.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import web.models.base as base
from web.models.base import BaseModel
#from web.models import storage
from web.models.schedule import Schedule
#from web.models.location import Location

node_schedules =Table(  "node_schedules",
                        Base.metadata,
                        Column("light_id", ForeignKey("lights.id"), primary_key=True),
                        Column("schedule_id", ForeignKey("schedules.id"), primary_key=True),)
class Light(BaseModel, Base):
    """
    Light node class

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

    __tablename__ = 'lights'
    brightnes = Column(Float(), nullable=True)
    location_id = Column(String(50), ForeignKey("locations.id"))
    schedules = relationship(   "Schedule",
                                secondary=node_schedules)

    def __init__(self, id, name, loc_id, brightnes=None, *args, **kwargs):
        """
        Init method for light nodes
        """

        super().__init__(id, name, *args, **kwargs)
        self.location_id = loc_id
        self.brightnes = brightnes

        storage.new(self)

    def get_schedules(self):
        """
        Get schedules associated with a light nodes
        """
        return self.schedules
