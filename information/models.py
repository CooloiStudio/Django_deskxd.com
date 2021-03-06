from django.db import models
from home.models import Languages

class Information(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    img = models.CharField(max_length=300)


class InformationInfo(models.Model):
    language = models.ForeignKey(Languages)
    infos = models.ForeignKey(Information)
    name = models.CharField(max_length=50)
    introduce = models.TextField(null=True)


class Protocol(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    url = models.CharField(max_length=500)


class ProtocolInfo(models.Model):
    language = models.ForeignKey(Languages)
    protocol = models.ForeignKey(Protocol)
    name = models.CharField(max_length=200)


class IBasePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    remark = models.TextField(null=True)

    def __unicode__(self):
        return self.name + "[" + self.remark + "]"


class InfoSection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.ForeignKey(IBasePage)


class InfoSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(InfoSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)