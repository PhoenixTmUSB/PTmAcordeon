# -*- coding: utf-8 -*-
import uuid
from django.db import models


class BaseAccordionManager(models.Manager):
    def get_queryset(self):
        return super(BaseAccordionManager, self).get_queryset().filter(parent=None)


class AccordionAbstract(models.Model):
    accordion_id = models.UUIDField(
        u'Id del acordeon',
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        u'Título',
        max_length=50
    )
    title_style = models.TextField(
        u'Estilos del Título',
        blank=True,
        null=True
    )
    content = models.TextField(
        u'Contenido',
        blank=True,
        null=True
    )
    content_style = models.TextField(
        u'Estilos del contenido',
        blank=True,
        null=True
    )
    width = models.CharField(
        u'Ancho (%)',
        max_length=50,
        blank=True,
        null=True,
        default='100'
    )
    height = models.CharField(
        u'Alto (px)',
        max_length=50,
        blank=True,
        null=True,
        default='30'
    )
    style = models.TextField(
        u'Estilos generales',
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class Accordion(AccordionAbstract):
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="panels"
    )

    # objects returns accordions that have no parent.
    # all_objects returns all accordions, with out without parents.
    objects = BaseAccordionManager()
    all_objects = models.Manager()

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.accordion_id)

    def get_child_panels(self):
        panels = Accordion.all_objects.filter(parent=self.id)
        return panels
