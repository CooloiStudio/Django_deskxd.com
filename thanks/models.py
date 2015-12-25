from django.db import models
from home.models import Languages

class Thanks(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)
    url = models.CharField(max_length=500)


class TBasePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    remark = models.TextField(null=True)

    def __unicode__(self):
        return self.name + "[" + self.remark + "]"


class TSection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.ForeignKey(TBasePage)


class TSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(TSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)