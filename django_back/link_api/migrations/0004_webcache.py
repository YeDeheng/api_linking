# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_api', '0003_auto_20160405_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('content', models.TextField()),
            ],
        ),
    ]