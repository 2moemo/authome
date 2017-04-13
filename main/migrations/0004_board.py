# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-13 07:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20170212_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('detail', models.TextField(verbose_name='내용')),
                ('count', models.IntegerField(verbose_name='조회수')),
                ('ip', models.GenericIPAddressField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '게시판',
            },
        ),
    ]
