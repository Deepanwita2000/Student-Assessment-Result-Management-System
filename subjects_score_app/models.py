from django.db import models
from studentapp.models import Student
from assessment_app.models import Assessment
# Create your models here.
class Subjects(models.Model):
    student=models.ForeignKey(Student , on_delete=models.CASCADE , related_name='subjects')
    maths = models.IntegerField(blank=True,null=True)
    physics = models.IntegerField(blank=True,null=True)
    chemistry = models.IntegerField(blank=True,null=True)
    english = models.IntegerField(blank=True,null=True)
    hindi = models.IntegerField(blank=True,null=True)
    bengali = models.IntegerField(blank=True,null=True)
    assessment = models.ForeignKey(Assessment , on_delete=models.CASCADE , related_name='subjects')
    total_marks = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    percentage = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return f"{self.student.email} - {self.percentage}"

class Grade(models.Model):
    grade=models.CharField(max_length=3)
    remark=models.CharField(max_length=250)
    emoji=models.CharField(max_length=250, blank=True,null=True)
    student=models.ForeignKey(Student , on_delete=models.CASCADE , related_name='grade')
    percentage = models.ForeignKey(Subjects , on_delete=models.CASCADE , related_name='grade') # subject

    def __str__(self):
        return f"{self.student.email} - {self.remark}"