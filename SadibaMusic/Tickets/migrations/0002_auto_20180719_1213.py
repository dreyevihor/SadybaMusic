# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='Event.Event'),
        ),
    ]
