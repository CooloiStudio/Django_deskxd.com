from django.db import models

class Contact(models.Model):
    email = models.CharField(max_length=100)
    sina = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    webpage = models.CharField(max_length=100)