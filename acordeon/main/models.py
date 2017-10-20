# -*- coding: utf-8 -*-
import uuid
from django.db import models


class AccordionAbstract(models.Model):
    acordion_id = models.UUIDField(
        u'Id del acordeon',
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        u'Título',
        max_length=50
    )
    title_style = models.TextField(
        blank=True,
        null=True
    )
    content = models.TextField(
        blank=True,
        null=True
    )
    content_style = models.TextField(
        blank=True,
        null=True
    )
    width = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='100'
    )
    height = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='30'
    )
    style = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class Accordion(AccordionAbstract):
    panels = models.ManyToManyField(
        'self',
        blank=True,
        related_name="panels",
    )

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.acordion_id)
