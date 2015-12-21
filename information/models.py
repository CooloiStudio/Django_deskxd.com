from django.db import models
from home.models import Languages

class Information(models.Model):
    code = models.IntegerField(unique=True)
    img = models.CharField(max_length=300)


class InformationInfo(models.Model):
    language = models.ForeignKey(Languages)
    infos = models.ForeignKey(Information)
    name = models.CharField(max_length=50)
    introduce = models.TextField(null=True)