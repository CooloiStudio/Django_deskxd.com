# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='info_id',
        ),
        migrations.RemoveField(
            model_name='information',
            name='menu_id',
        ),
    ]
