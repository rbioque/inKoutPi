# -*- coding: utf-8 -*-
# @proyect inKoutPi 
# config "entity"
__author__ = 'rbioque'

import sys

class ConfigAlert:

	def __init__(self, tem_alert_min, tem_alert_max, hum_alert_min, hum_alert_max, mail_alert):
		self.tem_alert_min = float(tem_alert_min)
		self.tem_alert_max = float(tem_alert_max)
		self.hum_alert_min = float(hum_alert_min)
		self.hum_alert_max = float(hum_alert_max)
		self.mail_alert = mail_alert

	def toDBCollection (self):
        	return {
            		"tem_alert_min":self.tem_alert_min,
            		"tem_alert_max":self.tem_alert_max,
            		"hum_alert_min":self.hum_alert_min,
            		"hum_alert_max":self.hum_alert_max,
			"mail_alert":self.mail_alert
        	}

	
	# Alerts
	
	def isTempAlertLessRange(self, temp):
                if temp <= self.tem_alert_min:
                        return True;
                return False;

	def isTempAlertGreaterRange(self, temp):
                if temp >= self.tem_alert_max:
                        return True;
                return False;
	
	def isHumAlertLessRange(self, hum):
		if hum > 1.0 and hum < self.hum_alert_min:
			return True;
		return False;

	def isHumAlertGreaterRange(self, hum):
		if hum > self.hum_alert_max:
			return True;
		return False;

	def isDoorOpen(self, hum):
		if hum == 1.0:
			return True;
		return False;


	# Info

	def getTemAlertMin(self):
		return self.tem_alert_min;

	def getTemAlertMax(self):
		return self.tem_alert_max;

	def getHumAlertMin(self):
		return self.hum_alert_min;

	def getHumAlertMax(self):
		return self.hum_alert_max;

	def getMailAlert(self):
		return self.mail_alert;

	def __str__(self):
        	return "Temp alert min: %s - Temp alert max: %s - Hum alert min: %s - Hum alert max: %s - Mail: %s" \
               %(self.tem_alert_min, self.tem_alert_max, self.hum_alert_min, self.hum_alert_max, self.mail_alert)
