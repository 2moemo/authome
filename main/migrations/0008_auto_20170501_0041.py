# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-30 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_macrolog_succeded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=70, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='macro',
            name='detail',
            field=models.TextField(verbose_name='간단한 설명'),
        ),
    ]
