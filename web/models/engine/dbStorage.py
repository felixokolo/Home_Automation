#!/usr/bin/python3
"""
Storage engine module
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from web.models.base import Base


class Storage:
	"""
	Database storage class
	"""

	engine = create_engine("mysql+mysqldb://alx:password@localhost/home_automation",
                            encoding='latin1', echo=True)
	
	Session = sessionmaker(bind=engine)
	session = Session()
