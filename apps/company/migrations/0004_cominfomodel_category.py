# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-20 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_cominfomodel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cominfomodel',
            name='category',
            field=models.CharField(blank=True, choices=[('0', '个体户'), ('1', '私企'), ('2', '国企'), ('3', '外资')], default='1', max_length=20, null=True, verbose_name='公司类型'),
        ),
    ]
