from django.db import models

class Information(models.Model):
    code = models.IntegerField(unique=True)
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    introduce = models.TextField(null=True)