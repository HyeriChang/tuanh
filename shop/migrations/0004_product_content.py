# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 05:59
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20171112_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
