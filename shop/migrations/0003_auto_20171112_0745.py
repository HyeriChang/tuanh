# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20171109_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_female',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_male',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
