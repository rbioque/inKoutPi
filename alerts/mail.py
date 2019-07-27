#!/usr/bin/python

# @proyect inKoutPi
# mail notification
__author__ = 'rbioque'

import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

class Mail:

	def __init__(self):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login("vperentie@gmail.com", "badrelition")

	def send(self, body, configAlert, config, measure):
		msg = MIMEMultipart()
		msg['From'] = "vperentie@gmail.com"
		msg['To'] = configAlert.getMailAlert()
		msg['Subject'] = config.getId() + ". Alert notification"	
		
		html = 	"<b>" + body + "</b><br/><br/>" + \
			"<b>Configuration</b><br/>" + config.__str__() + "<br/><br/>" + \
			"<b>Measure</b><br/>" + measure.__str__() + "<br/><br/>"
			 
		msgHtml = MIMEText(html, 'html')
		msg.attach(msgHtml)

		try:
			self.server.sendmail("inKoutPi@inKoutPi.es", configAlert.getMailAlert(), msg.as_string())
		except:
			print 'Error en envio de alerta. ', sys.exc_info()
		self.server.quit()

