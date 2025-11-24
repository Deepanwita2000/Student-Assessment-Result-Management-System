from django.contrib import admin

# Register your models here.
from .models import Assessment
# Register your models here.

class AsmtDetails(admin.ModelAdmin):
    list_display=[
    'type'
   
    ]
admin.site.register(Assessment,AsmtDetails)  