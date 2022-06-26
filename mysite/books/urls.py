from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact')
]

