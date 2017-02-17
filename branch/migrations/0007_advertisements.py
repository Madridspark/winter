# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_auto_20170213_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('link', models.TextField(default='', verbose_name='\u94fe\u63a5')),
                ('image', models.FileField(upload_to='./branch/ads-image-files/', verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u5e7f\u544a',
                'verbose_name_plural': '\u5e7f\u544a\u5217\u8868',
            },
        ),
    ]
