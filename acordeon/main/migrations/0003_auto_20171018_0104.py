# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171018_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='accordion',
            name='contet_style',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='accordion',
            name='title_style',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]