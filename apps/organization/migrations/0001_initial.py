# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-29 11:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u57ce\u5e02\u540d')),
                ('desc', models.CharField(max_length=200, verbose_name='\u63cf\u8ff0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '\u57ce\u5e02',
                'verbose_name_plural': '\u57ce\u5e02',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d')),
                ('desc', models.TextField(verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('num_class', models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u6570')),
                ('num_fav', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('image', models.ImageField(upload_to='org/%Y/%M', verbose_name='\u5c01\u9762\u56fe')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='\u6240\u5728\u57ce\u5e02')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u7ec4\u7ec7',
                'verbose_name_plural': '\u8bfe\u7a0b\u7ec4\u7ec7',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u8001\u5e08\u540d')),
                ('desc', models.TextField(verbose_name='\u8001\u5e08\u4ecb\u7ecd')),
                ('work_year', models.IntegerField(default=0, verbose_name='\u5de5\u4f5c\u5e74\u9650')),
                ('work_company', models.CharField(max_length=50, verbose_name='\u4efb\u804c\u516c\u53f8')),
                ('work_position', models.CharField(max_length=50, verbose_name='\u516c\u53f8\u804c\u4f4d')),
                ('points', models.CharField(max_length=10, verbose_name='\u6559\u5b66\u7279\u70b9')),
            ],
            options={
                'verbose_name': '\u6559\u5e08',
                'verbose_name_plural': '\u6559\u5e08',
            },
        ),
    ]
