# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170128_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
