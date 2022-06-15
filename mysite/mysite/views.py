from django.shortcuts import render
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render('current_time.html', {'current_time': now})

def hours_ahead(request, offset):
    offset = int(offset)
    time = datetime.datetime.now() + datetime.timedelta(hours=offset)
      

