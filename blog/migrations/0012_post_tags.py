# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170402_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='', max_length=400),
        ),
    ]
