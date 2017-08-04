# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0013_auto_20170713_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='citations',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='impact_factor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
