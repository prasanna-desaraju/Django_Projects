from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    diagnosis = models.TextField()
    treatment = models.TextField()
    admitted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
