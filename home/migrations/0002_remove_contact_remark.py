# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='remark',
        ),
    ]
