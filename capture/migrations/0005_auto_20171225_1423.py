# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0004_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='bookmark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='capture.Bookmark'),
        ),
    ]
