use inKoutPiDB

db.createCollection("CONFIG")
db.CONFIG.insert({ 	
	"tem_min": 30.00, 
	"tem_max": 30.10,
	"hum_min": 70,
	"hum_max": 100 
})

db.createCollection("HISTORY")


