# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-01-06 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20181229_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(default="", on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u6240\u5c5e\u673a\u6784'),
            preserve_default=False,
        ),
    ]