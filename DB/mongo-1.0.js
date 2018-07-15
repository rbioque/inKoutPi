use inKoutPiDB

db.createCollection("CONFIG")
db.CONFIG.insert({ 	
	"type": "CONFIG",
	"tem_min": 30.40, 
	"tem_max": 30.60,
	"hum_min": 70,
	"hum_max": 100 
})

db.CONFIG.insert({
	"type": "CONFIG_ALERT",         
	"tem_alert_min": 30.00,          
	"tem_alert_max": 31.00,           
	"hum_alert_min": 60,         
	"hum_alert_max": 120 
})

db.createCollection("HISTORY")


