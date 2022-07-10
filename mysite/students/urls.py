from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('hello/', views.hello),
    path('marksheet/<int:id>', views.marksheet)
]

