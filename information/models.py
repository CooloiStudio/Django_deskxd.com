from django.db import models

class Information(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    introduce = models.TextField(null=True)
    info_id = models.CharField(max_length=20)
    menu_id = models.CharField(max_length=20)