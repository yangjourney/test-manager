# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0004_auto_20170409_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]