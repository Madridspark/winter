# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0004_heroimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticinfo',
            name='theNotice',
            field=models.TextField(default='', verbose_name='\u7279\u522b\u5173\u6ce8'),
        ),
    ]