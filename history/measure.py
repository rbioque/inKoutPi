# -*- coding: utf-8 -*-
# @proyect inKoutPi
# measure for history
__author__ = 'rbioque'

import sys

class Measure:
	def __init__(self, tem, hum, date):
		self.tem = tem
		self.hum = hum
		self.date = date
		self.msg = None
		self.type = None
		
	def toDBCollection (self):
		if (self.msg is None and self.type is None):
                        return {
                                "tem":self.tem,
                                "hum":self.hum,
                                "date":self.date,
                        }

		else:
			return {
				"tem":self.tem,
				"hum":self.hum,
				"date":self.date,
				"msg":self.msg,
				"type":self.type
			}

	def getTemp(self):
		return self.tem;

	def getHumi(self):
		return self.hum;

	def getDate(self):
		return self.date;

	def setMsgType(self, msg, type):
		self.msg = msg;
		self.type = type;

	def getMsg(self):
		
		return self.msg;

	def getType(self):
		return self.type;

	def __str__(self):
		return "Temperature: %s - Humidity: %s - Date: %s - Msg: %s - Type: %s" \
			%(self.tem, self.hum, self.date, self.msg, self.type)
