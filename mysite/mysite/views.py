from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><title>Time</title><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><title>Time after</title><body>After %s hour(s), it'll be %s.</body></html>" % (offset, time)
    return HttpResponse(html)   
