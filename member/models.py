from django.db import models
from home.models import Languages

class Group(models.Model):
    sort = models.IntegerField(unique=True, default=0)
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Member(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    group = models.ForeignKey(Group)


class MemberInfo(models.Model):
    language = models.ForeignKey(Languages)
    member = models.ForeignKey(Member)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100, null=True)
    signature = models.CharField(max_length=200, null=True)


class MBasePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    remark = models.TextField(null=True)

    def __unicode__(self):
        return self.name + "[" + self.remark + "]"


class MSection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.ForeignKey(MBasePage)


class MSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(MSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)