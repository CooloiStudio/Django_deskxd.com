from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        permissions = (
            ("can_post", "Can post"),
        )

    def __unicode__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=60)
    url = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)