# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('introduce', models.TextField(null=True)),
                ('img', models.CharField(max_length=200)),
                ('signature', models.CharField(max_length=200)),
            ],
        ),
    ]
