# Generated by Django 2.0.5 on 2018-06-07 15:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_auto_20180606_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposals',
            name='is_blockchain',
            field=models.BooleanField(default=False, help_text='是否启用区块链', verbose_name='是否启用区块链'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(help_text='图片', upload_to='banner', verbose_name='轮播图片'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=0, help_text='轮播顺序', verbose_name='轮播顺序'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='proposals',
            field=models.ForeignKey(help_text='提案', on_delete=django.db.models.deletion.CASCADE, to='proposals.Proposals', verbose_name='提案'),
        ),
    ]
