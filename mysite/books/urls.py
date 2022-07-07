from pyexpat import model
from django.urls import path
from . import views
# from . import models

app_name = 'books'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_pages, name='about_pages'),
    path('publishers/', views.PulisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pub_id>', views.get_publisher, name='get_publisher'),
    path('hello/', views.generate_pdf),
    path('csv/', views.generate_csv)
]

