# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
