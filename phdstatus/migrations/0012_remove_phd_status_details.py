# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phdstatus', '0011_auto_20170727_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phd_status',
            name='details',
        ),
    ]
