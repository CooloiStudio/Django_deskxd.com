# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 08:17
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='Agreement')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
            ],
        ),
        migrations.CreateModel(
            name='ASection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('basepage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ASectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, null=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agreement.ASection')),
            ],
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='Privacy')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
            ],
        ),
        migrations.CreateModel(
            name='PSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('basepage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PSectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, null=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agreement.PSection')),
            ],
        ),
    ]
