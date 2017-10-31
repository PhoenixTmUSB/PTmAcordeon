# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accordion', '0010_merge_20171023_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='accordion',
            name='border_color',
            field=models.TextField(blank=True, null=True, verbose_name='Color del borde'),
        ),
        migrations.AddField(
            model_name='accordion',
            name='border_radius',
            field=models.TextField(blank=True, null=True, verbose_name='Radio del borde'),
        ),
        migrations.AddField(
            model_name='accordion',
            name='border_style',
            field=models.TextField(blank=True, null=True, verbose_name='Definir tipo de borde'),
        ),
        migrations.AddField(
            model_name='accordion',
            name='content_color',
            field=models.TextField(blank=True, null=True, verbose_name='Color del contenido'),
        ),
        migrations.AlterField(
            model_name='accordion',
            name='style',
            field=models.TextField(blank=True, null=True, verbose_name='Extra CSS'),
        ),
    ]
