# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-22 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ynm', '0002_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='desc',
            field=models.TextField(default='', null=True, verbose_name='备注'),
        ),
    ]
