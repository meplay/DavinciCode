# Generated by Django 2.0.5 on 2018-06-05 17:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_auto_20180605_1711'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProposalOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_amount', models.IntegerField(default=0, verbose_name='token数')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('proposal_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposals.ProposalOptions', verbose_name='提案')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户投票详情',
                'verbose_name_plural': '用户投票详情',
            },
        ),
        migrations.CreateModel(
            name='UserProposals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_amount', models.IntegerField(default=0, verbose_name='token数')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposals.Proposals', verbose_name='提案')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '交易信息',
                'verbose_name_plural': '交易信息',
            },
        ),
        migrations.CreateModel(
            name='UserSponsorProposals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='是否有效', verbose_name='是否有效')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('proposal', models.ForeignKey(help_text='提案id', on_delete=django.db.models.deletion.CASCADE, to='proposals.Proposals', verbose_name='提案')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户关注',
                'verbose_name_plural': '用户关注',
            },
        ),
        migrations.AlterModelOptions(
            name='userfav',
            options={'verbose_name': '用户关注', 'verbose_name_plural': '用户关注'},
        ),
        migrations.AlterUniqueTogether(
            name='usersponsorproposals',
            unique_together={('user', 'proposal')},
        ),
    ]
