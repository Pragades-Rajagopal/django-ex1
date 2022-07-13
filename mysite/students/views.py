import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from django.db.models import Sum, Avg
from django.db.models.functions import Round
from .models import Student, Marksheet

# Marksheet.objects.filter(student_id=1).values('student_id').annotate(total=Sum('mark'))
# Marksheet.objects.filter(student_id=1).values('student_id').annotate(avg=Round(Avg('mark')))

# Create your views here.
def hello(request):
    return HttpResponse('Hello students')

def marksheet(request, id):
    try:
        student = get_object_or_404(Student, pk=id)
        mark = Marksheet.objects.filter(student_id = student.id)
        t = Marksheet.objects.filter(student_id = student.id).values('student_id').annotate(total=Sum('mark'))
        a = Marksheet.objects.filter(student_id = student.id).values('student_id').annotate(avg=Round(Avg(('mark'))))
        
        # mark_list = [{'subject': mark[i]} for i in range(0, mark.count())]

        total = t[0]['total']
        avg = a[0]['avg']
        
        # return HttpResponse(json.dumps({'total': total, 'avg': avg}), content_type="application/json")
        return render(request, 'students/student_mark.html', {'total': total, 'avg': avg, 'student': student, 'marks': mark})

    except (IndexError):
        return render(request, 'students/student_mark.html', {'student': student, 'message': 'Marksheet not available'})



class student_list(ListView):
    model = Student
    context_object_name = 'student_list'

def student_page(request):
    try:
        student = Student.objects.all().order_by('-grade', 'name')
        mark_list = [
            {
                'student': student[i], 
                'mark_details': Marksheet.objects.filter(student_id= student[i].id),
                'total': Marksheet.objects.filter(student_id = student[i].id).values('student_id').annotate(total=Sum('mark'))
            }
            for i in range(0, student.count())
        ]
        # print(mark_list)
        
        return render(request, 'students/student_page.html', {'mark_list': mark_list})
    except:
        pass



