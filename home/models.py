from django.db import models


class Languages(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class IntroduceImage(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default=0)


class IntroduceInfo(models.Model):
    language = models.ForeignKey(Languages)
    image = models.ForeignKey(IntroduceImage)
    name = models.CharField(max_length=500, null=True)


class Menu(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)


class MenuInfo(models.Model):
    language = models.ForeignKey(Languages)
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=200)


class Contact(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    remark = models.CharField(max_length=100, default=0)


class ContactInfo(models.Model):
    language = models.ForeignKey(Languages)
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=200)
    text = models.TextField(null=True)
    img = models.CharField(max_length=500, null=True)
    url = models.CharField(max_length=200, null=True)


class BasePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    remark = models.TextField(null=True)

    def __unicode__(self):
        return self.name + "[" + self.remark + "]"


class Section(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    basepage = models.ForeignKey(BasePage)


class SectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(Section)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)