from django.db import models
from home.models import Languages

class Thanks(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)
    url = models.CharField(max_length=500)


class TSection(models.Model):
    code = models.IntegerField(unique=True)
    basepage = models.CharField(max_length=200)


class TSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(TSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)