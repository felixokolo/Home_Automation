#!/usr/bin/python3
"""
Base model for nodes
"""
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base = declarative_base()

class BaseModel():
    """
    Base class for nodes.

    ...
    Attributes
    ----------
    id : str
        Obeject ID
    created_at : Datetime
        Date and time object was created
    updated_at : Datetime
        Date and time object was updated

    """
    __instances = []  # stores all instances created
    __instanceNumber = 0  # counts the number of instances created

    def __init__(self, id, *args, **kwargs):
        """
        Init method for BaseModel class
        Args:
        id  : Integer
            Node ID
        """

        if type(id) is not str:  # id must be a string
            raise Exception("id must be a string")

        if id in BaseModel.__instances:  # id must be unique
            raise Exception("id already exists")

        self.id = id
        BaseModel.__instances.append(self.id)
        BaseModel.__instanceNumber += 1

        """instanciate using kwargs"""

        if kwargs != {}:
            ignore = ['id', 'class',]
            for k in kwargs:
                if k not in ignore:
                    """convert string formated time to datetime"""
                    if k in ['created_at', 'updated_at']:
                        self.__dict__[k] = datetime.strptime(kwargs[k], "%d/%m/%Y %H:%M:%S:%f")
                    else:
                        self.__dict__[k] = kwargs[k]
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts an Object instance to a dictionary
        Returns :
            dictionary containing all instance attributes
        """

        """copy instance attributes for modification"""
        to_return = self.__dict__.copy()

        """convert datetime to string formated time"""
        to_return['created_at'] = self.created_at.strftime("%d/%m/%Y %H:%M:%S:%f")
        to_return['updated_at'] = self.updated_at.strftime("%d/%m/%Y %H:%M:%S:%f")
        to_return['class'] = self.__class__.__name__
        return to_return
