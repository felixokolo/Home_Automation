#!/usr/bin/python3

"""
Model of channels
"""
from web.models.base import Base
from web.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from web.models.base import BaseModel
from web.models.schedule import Schedule
#from web.models.node import Node
import web.models as models

"""Many to many relationship table between channels and schedules"""

channels_schedules =Table(  "channels_schedules",
                            Base.metadata,
                            Column("channel_id", ForeignKey("channels.id"), primary_key=True),
                            Column("schedule_id", ForeignKey("schedules.id"), primary_key=True),)
class Channel(BaseModel, Base):
    """
    Channel class

    ...
    Attributes
    ----------
    __tablename__ : string
        Name of table
    node_id : string
        Associated node ID
    IO : string
        Input or Output
        possible values = ['IN', 'OUT']
    state : string
        Channel state
        possible values = ['ON', 'OFF', 'VAR']
    var_value : Float
        Variable value when state = VAR
    schedules : list
        List of ON or OFF schedules

    """

    __tablename__ = 'channels'
    var_value = Column(Float(), nullable=True)
    state = Column(String(50), nullable=False)
    IO = Column(String(50), nullable=False)
    node_id = Column(String(50), ForeignKey("nodes.id"))
    schedules = relationship(   "Schedule",
                                secondary=channels_schedules)

    def __init__(self, id, node_id, name=None, IO='OUT', state='OFF', var_value=0, *args, **kwargs):
        """
        Init method for node channels

        Args:

        id : string
            Channel id; must be specified during initialization
        name : string
            Channel name eg. Room Light
        node_id : string
            Associated node ID
        IO : string
            Input or Output
            possible values = ['IN', 'OUT']
        state : string
            Channel state
            possible values = ['ON', 'OFF', 'VAR']
        var_value : Float
            Variable value when state = VAR
        """

        if name is None:
            name = 'Channel_{}'.format(id)
        super().__init__(id, name, *args, **kwargs)
        self.node_id = node_id
        self.var_value = var_value
        self.IO = IO
        self.state = state

        models.storage.new(self)

    def get_schedules(self):
        """
        Get schedules associated with a light nodes
        """
        return self.schedules
