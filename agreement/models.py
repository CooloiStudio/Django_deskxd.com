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