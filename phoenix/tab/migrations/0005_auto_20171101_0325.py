# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0004_auto_20171101_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tab',
            name='order',
        ),
        migrations.AddField(
            model_name='tab',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tab.TabContainer'),
        ),
        migrations.AlterField(
            model_name='tab',
            name='border_color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Color del borde'),
        ),
        migrations.AlterField(
            model_name='tab',
            name='border_radius',
            field=models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Radio del borde (px)'),
        ),
        migrations.AlterField(
            model_name='tab',
            name='content_color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Color del contenido'),
        ),
    ]
