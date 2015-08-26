# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=20)),
                ('title_logo', models.CharField(max_length=20)),
                ('logo_color', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('default', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('image_url', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('value', models.TextField(null=True, blank=True)),
                ('info_class', models.CharField(max_length=20)),
                ('info_id', models.CharField(max_length=20)),
                ('txt_class', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('group', models.ForeignKey(to='home.Group')),
            ],
        ),
        migrations.CreateModel(
            name='IntroduceImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
