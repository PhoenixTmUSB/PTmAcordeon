# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accordion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acordeon_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('title_style', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('content_style', models.TextField(blank=True, null=True)),
                ('width', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('panels', models.ManyToManyField(blank=True, related_name='_accordion_panels_+', to='main.Accordion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
