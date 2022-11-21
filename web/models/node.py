#!/usr/bin/python3

"""
Model of nodes
"""
from web.models.base import Base
from web.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from web.models.base import BaseModel
from web.models.channel import Channel
import web.models as models

"""Many to many relationship table between nodes and channels"""
nodes_channels =Table(  "nodes_channels",
                        Base.metadata,
                        Column("node_id", ForeignKey("nodes.id"), primary_key=True),
                        Column("channel_id", ForeignKey("channels.id"), primary_key=True),)
class Node(BaseModel, Base):
    """
    Node class

    ...
    Attributes
    ----------
    __tablename__ : string
        Name of table
    name : string
            Node name eg. Room Node
    location_id : string
        Associated location ID
    state : string
        Node state
        possible values = ['ON', 'OFF']
    channels : relationship
        Table of nodes and associated channels

    """

    __tablename__ = 'nodes'
    state = Column(String(50), nullable=False)
    location_id = Column(String(50), ForeignKey("locations.id"))
    channels = relationship(   "Channel",
                                secondary=nodes_channels)

    def __init__(self, id, location_id, name=None, state='OFF', *args, **kwargs):
        """
        Init method for nodes

        Args:

        id : string
            Node id; must be specified during initialization
        name : string
            Node name eg. Room Node
        location_id : string
        	Associated location ID
        user_id : string
        	Associated user ID
    	state : string
        	Node state
        	possible values = ['ON', 'OFF']
        """

        if name is None:
            name = 'Node_{}'.format(id)
        super().__init__(id, name, *args, **kwargs)
        self.location_id = location_id
        self.state = state

        models.storage.new(self)

    def get_channels(self):
        """
        Get channels associated with node
        """
        return self.channels

    def add_channels(self, obj):
        """
        Associate a chanel with node

        Args:
        obj : Channel
            Channel to associate with node
        """
        self.channels.append(obj)

    @classmethod
    def get_loc_nodes(cls, loc_id):
        """
        Get all nodes associted to a Location id

        Args:
            loc_id : String
                location id to search
        """

        nodes = models.storage.get_class(cls.__name__);
        if nodes is None:
            return None
        return [node for node in nodes if node.location_id == loc_id]
