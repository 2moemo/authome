# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-22 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20170522_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='category',
            field=models.CharField(max_length=50, null=True, verbose_name='카테고리'),
        ),
    ]
