# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-16 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionmodel',
            name='name',
            field=models.CharField(max_length=100, verbose_name='岗位名称'),
        ),
        migrations.AlterField(
            model_name='skillmodel',
            name='name',
            field=models.CharField(max_length=100, verbose_name='技能名称'),
        ),
        migrations.AlterField(
            model_name='trademodel',
            name='trade_name',
            field=models.CharField(max_length=100, verbose_name='行业名称'),
        ),
    ]
