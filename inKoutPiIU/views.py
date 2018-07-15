from django.http import HttpResponse
from django.shortcuts import render

def monitoring(request):
	measure = {'temp': 30.0, 'humi': 99.0}
	return render(request, 'monitoring/index.html', measure)
