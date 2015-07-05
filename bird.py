#!/usr/bin/python2.7

from datetime import datetime

# local modules
from mongo import Mongo

class Bird():
	def __init__(self, name=None, family=None, continent=None, visible=False):
		self.name 		= name
		self.family 	= family
		self.continent	= continent
		self.visible	= visible
		self.M 			= Mongo()
	
	def list(self, id=None):
		""" Lists all birds if id is None.
			Lists one bird if id is set.
		"""
		if id is None:
			# get data from Mongo
			data = self.M.get()
			if not data:
				return False

			# Build a list of our object-id's
			response = []
			for b in data:
				if b['visible'] == True:
					response.append(str(b['_id']))

			# if we have any id's return to user
			if len(response) > 0:
				return response

			return False

		else:
			# get data from Mongo
			data = self.M.get(id)
			if not data:
				return False

			# here we convert _id to id for valid JSON
			data["id"] = str(data["_id"])
			# and pops the _id
			data.pop("_id")

			return data

		return False

	def insert(self):
		""" Creates our bird dict and ensures insertion.
		"""
		# create utc-date for when bird is added
		self.added = datetime.utcnow().strftime("%Y-%m-%d")

		# build our bird-dict
		bird = {
			"name": self.name, 
			"family": self.family, 
			"continents": self.continent, 
			"visible": self.visible, 
			"added": self.added
		}

		# insert bird
		id = self.M.insert(bird)

		return id

	def delete(self, id):
		""" Deletes the bird with supplied id from collection
		"""
		status = self.M.delete(id)

		# if deleted documents > 0 we've deleted the bird
		if status['n'] > 0:
			return True
		else:
			return False