# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0014_auto_20170804_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='page_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
