from django.db import models


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

    def __unicode__(self):
        return self.title

class GroupInfo(models.Model):
    group = models.ForeignKey(Group)
    code = models.IntegerField(unique=True, null=False)
    image_url = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=50, null=False)
    value = models.TextField(null=True, blank=True)
    info_class = models.CharField(null=False, max_length=20)
