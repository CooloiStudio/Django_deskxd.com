from django.db import models

class Members(models.Model):
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
