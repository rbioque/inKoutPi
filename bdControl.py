#!/usr/bin/python
# @proyect inKoutPi
# @autor rbioque
# Connection DB

import pymongo

connect_db()

def connect_db():
	from pymongo import MongoClient
	client = MongoClient('localhost', 27017)
	db = client.inKoutPiDB
	return;

def find_config():
	config = db.CONFIG.find()
	return config;

	

