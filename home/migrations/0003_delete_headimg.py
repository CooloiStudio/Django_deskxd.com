# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_headimg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeadImg',
        ),
    ]
