from django.db import models


class IntroduceImage(models.Model):
    code = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=100)
