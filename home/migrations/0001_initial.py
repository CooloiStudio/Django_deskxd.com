# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField(null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='IntroduceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('url', models.CharField(max_length=100)),
                ('img', models.CharField(default=0, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='IntroduceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.IntroduceImage')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('basepage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, null=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Section')),
            ],
        ),
        migrations.AddField(
            model_name='introduceinfo',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages'),
        ),
    ]
