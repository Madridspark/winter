# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0007_advertisements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='image',
            field=models.FileField(upload_to='./branch/ads-files/image/', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='link',
            field=models.FileField(upload_to='./branch/ads-files/text/', verbose_name='\u4ecb\u7ecd\u6587\u4ef6'),
        ),
    ]
