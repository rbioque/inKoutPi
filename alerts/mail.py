#!/usr/bin/python

# @proyect inKoutPi
# mail notification
__author__ = 'rbioque'

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

class Mail:

	def __init__(self):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login("raul.bioque@gmail.com", "badrelition##3")

	def send(self, body):
		msg = MIMEMultipart()
		msg['From'] = "raul.bioque@gmail.com"
		msg['To'] = "raul.bioque@gmail.com"
		msg['Subject'] = "inKoutPi alert notification"	
		
		html = """\
    			<p>This is an inline image<br/>
        			<img src="cid:image1">
    			</p>
		"""
		msgHtml = MIMEText(html, 'html')

		img = open('/home/pi/inKoutPi/alerts/avatar.png', 'rb').read()
    		msgImg = MIMEImage(img, 'png')
    		msgImg.add_header('Content-ID', '<image1>')
    		msgImg.add_header('Content-Disposition', 'inline', filename='/home/pi/inKoutPi/alerts/avatar.png')
		
		msg.attach(msgHtml)
		msg.attach(msgImg)

		self.server.sendmail("inKoutPi@inKoutPi.es", "raul.bioque@gmail.com", msg.as_string())
		self.server.quit()

