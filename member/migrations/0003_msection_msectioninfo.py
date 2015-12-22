# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20151221_0931'),
        ('member', '0002_auto_20151221_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('basepage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MSectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, null=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.MSection')),
            ],
        ),
    ]
