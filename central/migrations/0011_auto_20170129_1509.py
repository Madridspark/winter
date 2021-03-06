# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0010_auto_20170129_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticinfo',
            name='theAddress',
            field=models.CharField(default=1234567890, max_length=256, verbose_name='\u5730\u5740'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='theEmail',
            field=models.CharField(default=23456578, max_length=256, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='thePostcode',
            field=models.CharField(default=123456, max_length=256, verbose_name='\u90ae\u7f16'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='theTEL',
            field=models.CharField(default=710021, max_length=256, verbose_name='\u7535\u8bdd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heroimages',
            name='theHeroTitle',
            field=models.CharField(max_length=256, unique=True, verbose_name='\u6807\u9898'),
        ),
    ]
