# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phdstatus', '0005_auto_20170718_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('duration', models.CharField(max_length=100, verbose_name='Duration')),
                ('phd_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phdstatus.phd_status')),
            ],
        ),
    ]
