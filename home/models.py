from django.db import models


class IntroduceImage(models.Model):
    code = models.IntegerField(null=False, unique=True)
    url = models.CharField(max_length=100)
