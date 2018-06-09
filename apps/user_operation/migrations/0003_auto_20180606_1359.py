# Generated by Django 2.0.5 on 2018-06-06 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20180605_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='building',
            field=models.CharField(default='', help_text='幢', max_length=100, verbose_name='幢'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='code',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='小区'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='community',
            field=models.CharField(default='', help_text='社区', max_length=100, verbose_name='小区'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='room',
            field=models.CharField(default='', help_text='室', max_length=100, verbose_name='室'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='unit',
            field=models.CharField(default='', help_text='单元', max_length=100, verbose_name='单元'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address',
            field=models.CharField(default='', help_text='提案id', max_length=100, verbose_name='详细地址'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default='', help_text='市', max_length=100, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='district',
            field=models.CharField(default='', help_text='区', max_length=100, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='province',
            field=models.CharField(default='', help_text='省', max_length=100, verbose_name='省份'),
        ),
    ]
