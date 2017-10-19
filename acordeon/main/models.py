from django.db import models

from decimal import Decimal



class AccordionAbstract(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    title_style = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_style = models.TextField(blank=True, null=True)
    width = models.CharField(max_length=50, blank=True, null=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    style = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class SubAccordion(AccordionAbstract):

    def get_name_for_id(self):
        return self.name.replace(" ", "")

    def __str__(self):
        return self.name


class Accordion(AccordionAbstract):
    sub_accordions = models.ManyToManyField(
        SubAccordion,
        blank=True,
        related_name="accordion_sub_accordions"
    )

    def get_name_for_id(self):
        return self.name.replace(" ", "")

    def __str__(self):
        return self.name
