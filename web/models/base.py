#!/usr/bin/python3
"""
Base model for nodes
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

class BaseModel(Base):
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
