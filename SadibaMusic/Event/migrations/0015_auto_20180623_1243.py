# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-23 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0014_auto_20180623_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_portfolio',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_images', to='Event.Event'),
        ),
    ]
