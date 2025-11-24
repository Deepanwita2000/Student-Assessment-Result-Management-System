from django.db import models

# Create your models here.
class Student(models.Model):
    HINDI = 'hindi'
    BENGALI = 'bengali'
   
    ROLE_CHOICES=[
        ( 'hindi','Hindi'),
        ('bengali','Bengali')
    ]
    gender_choices=[
         ( 'male','Male'),
         ( 'female','Female'),
    ]
    city_choices=[
        ('kolkata' , 'Kolkata'),
        ('darjeeling' , 'Darjeeling'),
        ('siliguri' , 'Siliguri'),
        ('howrah' , 'Howrah'),
        ('haldia' , 'Haldia'),
        ('durgapur' , 'Durgapur'),
        ('jalpaiguri' , 'Jalpaiguri'),
        ('santipur' , 'Santipur'),
    ]
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    # physics = models.IntegerField()
    # maths   = models.IntegerField()
    # computer   = models.IntegerField()
    gender = models.CharField(max_length=10 , choices=gender_choices)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100 , choices=city_choices)
    language = models.CharField(max_length=50 , choices=ROLE_CHOICES)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.email
    


# from django.db import models

# # Create your models here.
# class Student(models.Model):
#     Role_Choices=[
#         ('Hindi', 'hindi'),
#         ('Bengali', 'bengali')
#     ]
#     first_name = models.CharField(max_length=100)
#     lastt_name = models.CharField(max_length=100)
#     email=models.EmailField(unique=True)
#     # score = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     city = models.CharField(max_length=100)
#     language = models.CharField(max_length=50 , choices=Role_Choices)
#     contact = models.IntegerField(max_length=10)

#     def __str__(self):
#         return self.email
    

    



