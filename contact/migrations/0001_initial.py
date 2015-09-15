# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('sina', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('webpage', models.CharField(max_length=100)),
            ],
        ),
    ]
