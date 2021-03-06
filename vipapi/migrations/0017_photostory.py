# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-18 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapi', '0016_vipwinner_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photourl', models.ImageField(max_length=2500, upload_to=b'uploadedimages')),
                ('description', models.TextField(null=True)),
                ('dateadded', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'PhotoStory',
            },
        ),
    ]
