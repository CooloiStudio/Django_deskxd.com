from django.db import models
from home.models import Languages

class Games(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    img = models.CharField(max_length=200)
    url = models.CharField(max_length=100)


class GameInfo(models.Model):
    language = models.ForeignKey(Languages)
    games = models.ForeignKey(Games)
    name = models.CharField(max_length=50)
    abstract = models.CharField(max_length=150)
    introduce = models.TextField(null=True)


class GameImages(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    img = models.CharField(max_length=300)
    url = models.CharField(max_length=300)


class GBasePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    remark = models.TextField(null=True)

    def __unicode__(self):
        return self.name + "[" + self.remark + "]"


class GSection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.ForeignKey(GBasePage)


class GSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(GSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
