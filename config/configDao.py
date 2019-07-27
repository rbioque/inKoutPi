# @proyect inKoutPi
# config dao
__author__ = 'rbioque'

import pymongo
from . import config
from . import configAlert

class ConfigDao:

	def __init__(self):
		# Making connection with MongoGlient
		from pymongo import MongoClient
		client = MongoClient('localhost', 27017)
		self.db = client.inKoutPiDB

	def find(self):
		r = self.db.CONFIG.find_one({'type': "CONFIG"})
		c = config.Config(r['id'], r['tem_min'], r['tem_max'],r['hum_min'],r['hum_max'])
		return c;
	
	def findJSON(self):
		return self.db.CONFIG.find_one({'type': "CONFIG"})
			
	def findAlert(self):
		r = self.db.CONFIG.find_one({'type': "CONFIG_ALERT"})
		c = configAlert.ConfigAlert(r['tem_alert_min'], r['tem_alert_max'],r['hum_alert_min'],r['hum_alert_max'],r['mail_alert'])
		return c;

	def findAlertJSON(self):
		return self.db.CONFIG.find_one({'type': "CONFIG_ALERT"})

	def merge(self, config):
		self.db.CONFIG.update({'type': "CONFIG"}, {'$set': config.toDBCollection()})

	def mergeAlert(self, configAlert):
		self.db.CONFIG.update({'type': "CONFIG_ALERT"}, {'$set': configAlert.toDBCollection()})
		
