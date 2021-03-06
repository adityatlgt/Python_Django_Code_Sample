# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-27 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapi', '0010_auto_20190120_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescribeYourself',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('selftext', models.TextField(max_length=2000)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'DescribeYourself',
            },
        ),
    ]
