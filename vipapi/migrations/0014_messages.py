# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-05 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapi', '0013_remove_applicantstatus_profilecompleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=2000)),
                ('messagedate', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
