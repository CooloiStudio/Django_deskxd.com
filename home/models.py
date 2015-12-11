from django.db import models


class Languages(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)


class IntroduceImage(models.Model):
    code = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default=0)
