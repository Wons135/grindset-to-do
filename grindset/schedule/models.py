from django.db import models

# Create your models here.

class Schedule(models.Model):
    date        = models.DateField()
    hour        = models.TimeField()
    type        = models.CharField(max_length = 16)
    description = models.TextField()
    status      = models.BooleanField(default = 0)