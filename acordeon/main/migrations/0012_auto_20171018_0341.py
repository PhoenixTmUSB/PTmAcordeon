# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20171018_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='accordion',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subaccordion',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
