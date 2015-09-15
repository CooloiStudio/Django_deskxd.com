from django.db import models

class Members(models.Model):
    group = models.IntegerField(default=1,null=False)
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    introduce = models.TextField(null=True)
    img = models.CharField(max_length=200)
