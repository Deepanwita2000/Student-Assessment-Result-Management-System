from django.db import models

# Create your models here.
class Assessment(models.Model):
    exam_choices=[
        ('assessment 1','Assessment 1'),
        ('assessment 2','Assessment 2'),
        ('assessment 3','Assessment 3'),
        ('assessment 4','Assessment 4'),
    ]
    type = models.CharField(max_length=20, choices=exam_choices)
    
    def __str__(self):
        return self.type