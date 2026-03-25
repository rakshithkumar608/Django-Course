from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerFiels()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    
    
    