#!/usr/bin/python3
"""
Storage engine module
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from web.models.channel import Channel
from web.models.node import Node
from web.models.location import Location
from web.models.schedule import Schedule
from web.models.user import User
from web.models.base import Base


class Storage:
	"""
	Database storage class
	"""

	__engine = create_engine("mysql+mysqldb://alx:password@localhost/home_automation",
                            encoding='latin1', echo=True)

	__Session = sessionmaker(bind=__engine)
	__session = __Session()
	psession = __Session()
	__classes = ['Node', 'Schedule', 'Location', 'User', 'Channel']

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
		try:
			Base.metadata.create_all(self.__engine)
			self.__session.commit()
		except Exception as e:
			print(e)
			raise Exception(e)

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

	def get_class(self, cls):
		"""
		Get object of specified class

		Args:
		cls : String
			Name of class
		"""
		ret = self.__session.query(eval(cls)).all()
		if len(ret) != 0:
			return ret
		return None

	def delete_all(self):
		"""
		Get object of specified class

		Args:
		cls : String
			Name of class
		"""
		for cls in self.__classes:
			self.__session.query(eval(cls)).delete()
		self.__session.commit()
