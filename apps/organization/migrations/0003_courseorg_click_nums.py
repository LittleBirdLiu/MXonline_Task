# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-12-29 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorg_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]
