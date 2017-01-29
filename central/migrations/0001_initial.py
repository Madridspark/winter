# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theName', models.CharField(max_length=256, verbose_name='\u672c\u7ad9\u540d\u79f0')),
                ('theIntro', models.TextField(default='', verbose_name='\u672c\u7ad9\u7b80\u4ecb')),
            ],
            options={
                'verbose_name': '\u672c\u7ad9\u4fe1\u606f',
                'verbose_name_plural': '\u672c\u7ad9\u4fe1\u606f',
            },
        ),
    ]
