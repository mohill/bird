#!/usr/bin/python2.7
"""
Class for dealing with mongo-database.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class Mongo():
	def __init__(self):
		""" Initiates the Mongo class.
			It uses self.connect() to connect and store collection-handler in
			self.bird.
		"""
		self.bird 		= self.connect()

	def connect(self):
		""" Connects to the database on localhost and returns the collection
			bird.
		"""
		client = MongoClient('mongodb://localhost:27017/')
		db = client.bird
		bird = db.bird
		return bird

	def get(self, id=None):
		""" Get bird from collection.
		"""
		if id is None:
			birds = self.bird.find()
			return birds
		else:
			bird = self.bird.find_one({'_id' : ObjectId(id)})
			return bird

	def insert(self, json):
		""" Insert bird into collection
		"""
		return self.bird.insert_one(json).inserted_id

	def delete(self, id):
		""" Delete bird from collection
		"""
		return self.bird.remove({'_id': ObjectId(id)})
