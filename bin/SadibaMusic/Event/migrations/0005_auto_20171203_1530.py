# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_auto_20171202_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='afisha_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='image_portfolio',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
