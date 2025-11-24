
from django.contrib import admin
from django.urls import  path
from . import views
urlpatterns = [

    path('view_marks/' , views.view_marks , name='view_marks'),
    path('add_marks/' , views.add_marks , name='add_marks'),
    path('edit_marks/<int:pk>/' , views.edit_marks , name='edit_marks'),
    path('delete_marks/<int:pk>/' , views.delete_marks , name='delete_marks'),
    path('view_student_records/' , views.view_student_records , name='view_student_records'),

  
]
