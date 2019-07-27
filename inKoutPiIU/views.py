import sys
import os
#import json

from bson import BSON
from bson import json_util
from bson.json_util import loads, dumps
#from json import loads, dumps
#import ujson
#import bsonjs

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .forms import ConfigForm, ConfigAlertForm

sys.path.insert(0, '../')
from history import historyDao
from config import configDao, config, configAlert

def monitoring(request):
	hisDao = historyDao.HistoryDao()
	cnfDao = configDao.ConfigDao()

	aux = hisDao.findLastsMeasure(10)
	last = aux[0]
	lasts = dumps(aux)
	conf = dumps(cnfDao.findJSON(), ensure_ascii=False) 

	return render(request, 'monitoring/index.html', {'last': last, 'lasts': lasts, 'conf': conf})

def alerts(request):
	hisDao = historyDao.HistoryDao()
	alerts = loads(dumps(hisDao.findAlerts(500)))
	return render(request, 'alerts/alerts.html', {'alerts': alerts})

def history(request):
	hisDao = historyDao.HistoryDao()
	history = loads(dumps(hisDao.findLastsOnlyMeasure(500)))
	return render(request, 'history/history.html', {'history': history})

def conf(request):
	cnfDao = configDao.ConfigDao()
	if request.method == 'POST':
		form = ConfigForm(request.POST)
		formAlert = ConfigAlertForm(request.POST)
		
		if form.is_valid() and formAlert.is_valid():
			cnfDao.merge(config.Config(str(form.cleaned_data['id']), str(form.cleaned_data['tem_min']), str(form.cleaned_data['tem_max']), str(form.cleaned_data['hum_min']), str(form.cleaned_data['hum_max'])))
			cnfDao.mergeAlert(configAlert.ConfigAlert(str(formAlert.cleaned_data['tem_alert_min']), str(formAlert.cleaned_data['tem_alert_max']), str(formAlert.cleaned_data['hum_alert_min']), str(formAlert.cleaned_data['hum_alert_max']), str(formAlert.cleaned_data['mail_alert'])))
			messages.add_message(request, messages.INFO, 'Configuración guardada correctamente!')
		else:
			if form.is_valid():
				messages.add_message(request, messages.ERROR, formAlert.errors)
			else:	
				messages.add_message(request, messages.ERROR, form.errors)

	jconfig = loads(dumps(cnfDao.findJSON()))
	jconfigAlert = loads(dumps(cnfDao.findAlertJSON()))

	form = ConfigForm(initial=jconfig)	
	formAlert = ConfigAlertForm(initial=jconfigAlert)

	return render(request, 'config/config.html', {'form': form, 'formAlert': formAlert, 'config': jconfig, 'configAlert': jconfigAlert})

