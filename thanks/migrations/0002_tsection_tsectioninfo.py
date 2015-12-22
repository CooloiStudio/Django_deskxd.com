# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20151221_0931'),
        ('thanks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('basepage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TSectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, null=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thanks.TSection')),
            ],
        ),
    ]
