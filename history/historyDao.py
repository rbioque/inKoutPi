# @proyect inKoutPi
# history dao
__author__ = 'rbioque'

import pymongo
pymongo.has_c()
from . import measure

class HistoryDao:

	def __init__(self):
		# Making connection with MongoGlient
		from pymongo import MongoClient
		client = MongoClient('localhost', 27017)
		self.db = client.inKoutPiDB

	def persist(self, measure):
		self.db.HISTORY.insert(measure.toDBCollection())

	def findLastMeasure(self):
		measure = self.db.HISTORY.find().sort("date", -1).limit(1)
		return measure;

	def findLastsMeasure(self, rows):
		measures = self.db.HISTORY.find().sort("date", -1).limit(rows)
		return measures;

	def findLastsOnlyMeasure(self, rows):
		measures = self.db.HISTORY.find({ "msg": { "$exists": False } }).sort("date", -1).limit(rows)
		return measures;

	def findAlerts(self, rows):
		alerts = self.db.HISTORY.find({ "msg": { "$exists": True } }).sort("date", -1).limit(rows)
		return alerts;
