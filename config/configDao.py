# @proyect inKoutPi
# config dao
__author__ = 'rbioque'

import pymongo

class ConfigDao:

	def __init__(self):
		# Making connection with MongoGlient
		print("init de dao")
		from pymongo import MongoClient
		client = MongoClient('localhost', 27017)
		self.db = client.inKoutPiDB

	def find_config(self):
		config = self.db.CONFIG.find()
		for c in config:
			print(c)
		return c;

	def update_config(self, config):
		return config;

	def test(self):
		print('test ok')
