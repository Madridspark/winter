# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0006_heroimages_theimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroimages',
            name='theHref',
        ),
        migrations.AddField(
            model_name='heroimages',
            name='theHeroTitle',
            field=models.CharField(default=0, max_length=256, verbose_name='\u6807\u9898'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heroimages',
            name='theImage',
            field=models.FileField(upload_to='./header/', verbose_name='\u4e0a\u4f20\u6587\u4ef6'),
        ),
    ]
