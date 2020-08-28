from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	city  = "Hyderabad"
	state = "Telangana"
	context = {"city":city, "state":state}
	return render(request,'index.html', context)
	