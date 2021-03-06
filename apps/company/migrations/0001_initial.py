# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts_name', models.CharField(default='', max_length=100, verbose_name='联系人姓名')),
                ('position', models.CharField(blank=True, max_length=30, verbose_name='岗位')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='联系电话')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='快递地址')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '联系信息',
                'verbose_name_plural': '联系信息',
            },
        ),
        migrations.CreateModel(
            name='ComInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='公司名称')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='公司地址')),
                ('credit_no', models.CharField(blank=True, default='', max_length=100, verbose_name='信用代码')),
                ('desc', models.TextField(default='', verbose_name='公司简介')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('trade', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='position.TradeModel', verbose_name='所属行业')),
            ],
            options={
                'verbose_name': '公司信息',
                'verbose_name_plural': '公司信息',
            },
        ),
        migrations.CreateModel(
            name='ComRecruitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='所在城市')),
                ('skill', models.CharField(blank=True, default='', help_text='一级瓦工', max_length=30, verbose_name='技能等级')),
                ('desc', models.TextField(blank=True, default='', null=True, verbose_name='岗位描述')),
                ('num', models.IntegerField(default=1, verbose_name='招聘人数')),
                ('min_salary', models.IntegerField(default='', help_text='每月工资', verbose_name='最低薪资')),
                ('max_salary', models.IntegerField(default='', help_text='每月工资', verbose_name='最高薪资')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.ComInfoModel', verbose_name='公司')),
                ('position', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='position.PositionModel', verbose_name='岗位')),
            ],
            options={
                'verbose_name': '招聘信息',
                'verbose_name_plural': '招聘信息',
            },
        ),
        migrations.AddField(
            model_name='comcontactmodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.ComInfoModel', verbose_name='公司'),
        ),
    ]
