# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-28 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmg', '0002_newworkermodel_peo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newworkermodel',
            name='img',
            field=models.ImageField(blank=True, default='img/default2.jpg', max_length=200, null=True, upload_to='img/%Y/%m', verbose_name='头像'),
        ),
    ]