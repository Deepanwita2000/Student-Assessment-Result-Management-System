
from django.contrib import admin
from django.urls import  path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('student/', include('studentapp.urls')),
    path('subjects/', include('subjects_score_app.urls')),
]
  