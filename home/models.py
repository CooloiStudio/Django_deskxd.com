from django.db import models

class BaseHtml(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Site(models.Model):
    code = models.IntegerField(null=False, unique=True)
    class_name = models.CharField(max_length=50, null=True)
    id_name = models.CharField(max_length=50, null=True)
    base_page = models.ForeignKey(BaseHtml)
    default = models.BooleanField(default=True)
    value = models.TextField(null=True, blank=True)

class SiteTitle(models.Model):
    name = models.CharField(max_length=50)
    default = models.BooleanField(default=False)

class IntroduceImage(models.Model):
    code = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=20, null=False)
    url = models.CharField(max_length=100)

class Group(models.Model):
    code = models.IntegerField(null=False, unique=True)
    title = models.CharField(max_length=20, null=False)
    title_img = models.CharField(max_length=50, null=False)
    url = models.CharField(max_length=50, null=False)
    group_class = models.CharField(max_length=20, null=False)

class GroupInfo(models.Model):
    group = models.ForeignKey(Group)
    code = models.IntegerField(unique=True, null=False)
    image_url = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=50, null=False)
    value = models.TextField(null=True, blank=True)
    info_class = models.CharField(null=False, max_length=20)

    def __unicode__(self):
        return self.title

class PoweredBy(models.Model):
    code = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)

class Menu(models.Model):
    code = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
