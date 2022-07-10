import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Sum, Avg
from django.db.models.functions import Round
from .models import Student, Marksheet

# Marksheet.objects.filter(student_id=1).values('student_id').annotate(total=Sum('mark'))
# Marksheet.objects.filter(student_id=1).values('student_id').annotate(avg=Round(Avg('mark')))

# Create your views here.
def hello(request):
    return HttpResponse('Hello students')

def marksheet(request, id):
    student = get_object_or_404(Student, pk=id)
    t = Marksheet.objects.filter(student_id = student.id).values('student_id').annotate(total=Sum('mark'))
    a = Marksheet.objects.filter(student_id = student.id).values('student_id').annotate(avg=Round(Avg(('mark'))))

    total = t[0]['total']
    avg = a[0]['avg']
    
    return HttpResponse(json.dumps({'total': total, 'avg': avg}), content_type="application/json")



