# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-09 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170509_1750'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
