# @proyect inKoutPi
# config dao
__author__ = 'rbioque'

import pymongo
import config

class ConfigDao:

	def __init__(self):
		# Making connection with MongoGlient
		from pymongo import MongoClient
		client = MongoClient('localhost', 27017)
		self.db = client.inKoutPiDB

	def find(self):
		r = self.db.CONFIG.find_one()
		c = config.Config(r['tem_min'], r['tem_max'],r['hum_min'],r['hum_max'])
		return c;
		
