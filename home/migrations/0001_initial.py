# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseHtml',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=20)),
                ('title_img', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('group_class', models.CharField(max_length=20)),
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
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PoweredBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('class_name', models.CharField(max_length=50, null=True)),
                ('id_name', models.CharField(max_length=50, null=True)),
                ('default', models.BooleanField(default=True)),
                ('value', models.TextField(null=True, blank=True)),
                ('base_page', models.ForeignKey(to='home.BaseHtml')),
            ],
        ),
        migrations.CreateModel(
            name='SiteTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('default', models.BooleanField(default=False)),
            ],
        ),
    ]
