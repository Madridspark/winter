# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0025_auto_20170217_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staticabout',
            name='theName',
        ),
    ]
