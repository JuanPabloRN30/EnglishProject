# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0002_auto_20171107_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='letter',
            field=models.TextField(),
        ),
    ]
