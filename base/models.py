from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Period(models.Model):
    startTime = models.CharField(max_length=20)
    endTime = models.CharField(max_length=20)
    courseCode = models.CharField(max_length=10)
    isTheory = models.BooleanField()
    # courseTeachers = ArrayField(models.CharField(max_length=10))