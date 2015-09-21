# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('img', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('abstract', models.CharField(max_length=150)),
                ('introduce', models.TextField(null=True)),
            ],
        ),
    ]