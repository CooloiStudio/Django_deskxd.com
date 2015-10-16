from django.db import models

class Thanks(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
