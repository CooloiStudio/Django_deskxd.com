from django.db import models

class Games(models.Model):
    code = models.IntegerField(unique=True)
    img = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    introduce = models.TextField(null=True)
