from django.db import models

# Create your models here.

class student(models.Model):
    Name = models.CharField(max_length=10)
    Roll=models.IntegerField()
