from django.contrib import admin
from django.urls import  path
from . import views
urlpatterns = [

    path('' , views.read_student , name='read_student'),
    path('create/' , views.create_student , name='create_student'),
    path('search_student/' , views.search_student , name='search_student'),
    path('edit/<int:x>' , views.edit_student , name='edit_student'),
    path('delete/<int:dX>/' , views.delete_student , name='delete_student'),


  
  
]
