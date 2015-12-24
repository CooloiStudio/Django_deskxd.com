from django.db import models
from DjangoUeditor.models import UEditorField
from home.models import Languages

class Agreement(models.Model):
    title = models.CharField(max_length=200)
    language = models.ForeignKey(Languages)
    content = UEditorField(u'Agreement', width=1200, height=600, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000}, settings={}, command=None, blank=True)

class Privacy(models.Model):
    title = models.CharField(max_length=200)
    language = models.ForeignKey(Languages)
    content = UEditorField(u'Privacy', width=1200, height=600, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000}, settings={}, command=None, blank=True)


class ASection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.CharField(max_length=200)


class ASectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(ASection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)


class PSection(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.CharField(max_length=200)


class PSectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(PSection)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)