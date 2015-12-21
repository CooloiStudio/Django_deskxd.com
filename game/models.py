from django.db import models
from home.models import Languages

class Games(models.Model):
    code = models.IntegerField(unique=True)
    img = models.CharField(max_length=200)
    url = models.CharField(max_length=100)


class GameInfo(models.Model):
    language = models.ForeignKey(Languages)
    games = models.ForeignKey(Games)
    name = models.CharField(max_length=50)
    abstract = models.CharField(max_length=150)
    introduce = models.TextField(null=True)


class GameImages(models.Model):
    code = models.IntegerField(unique=True, default=0)
    img = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
