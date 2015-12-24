from django.db import models
from home.models import Languages


class Member(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)
    img = models.CharField(max_length=200)


class MemberInfo(models.Model):
    language = models.ForeignKey(Languages)
    member = models.ForeignKey(Member)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100, null=True)
    signature = models.CharField(max_length=200, null=True)


class MSection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.CharField(max_length=200)


class MSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(MSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)