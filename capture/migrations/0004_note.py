# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0003_bookmark_foldername'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=40)),
                ('y', models.CharField(max_length=40)),
                ('text', models.TextField(default='')),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capture.Bookmark')),
            ],
        ),
    ]
