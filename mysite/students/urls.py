from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('hello/', views.hello),
    path('list/', views.student_list.as_view(), name='student_list'),
    path('marksheet/<int:id>', views.marksheet, name='marksheet'),
    path('marksheet/<int:id>', views.marksheet, name='get_marks'),
    path('page/', views.student_page, name='student_page')
]

