#!/usr/bin/python3
"""
Storage engine module
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from web.models.lightNodes import Light
from web.models.base import Base


class Storage:
	"""
	Database storage class
	"""

	__engine = create_engine("mysql+mysqldb://alx:password@localhost/home_automation",
                            encoding='latin1', echo=True)

	__Session = sessionmaker(bind=__engine)
	__session = __Session()

	def __init__(self):
		"""
		Init for storage class
		"""
		Base.metadata.create_all(self.__engine)

	def new(self, obj):

		"""
		Adds object to transaction

		Args:
			obj : object
				object to add to database
		"""
		self.__session.add(obj)

	def save(self):

		"""
		Executes pending transactions
		"""
		Base.metadata.create_all(self.__engine)
		self.__session.commit()

	def get(self, cls, id):
		"""
		Get object of specified class and id

		Args:
		cls : String
			Name of class
		id : string
			ID of object
		"""
		ret = self.__session.query(eval(cls)).filter(eval(cls).id == id).all()
		if len(ret) != 0:
			return ret[0]
		return None
