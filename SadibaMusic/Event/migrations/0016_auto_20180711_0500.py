# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0015_auto_20180623_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
