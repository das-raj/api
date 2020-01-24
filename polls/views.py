from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

def todays_date(request):
    current_date = date.today()
    server_name = 'Server1'
    return HttpResponse("Today's date is "+str(current_date)+" ("+server_name+")")
