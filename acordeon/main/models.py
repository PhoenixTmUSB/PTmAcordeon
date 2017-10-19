from django.db import models


class AccordionAbstract(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    title = models.CharField(max_length=50, blank=True, default='')
    title_style = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    contet_style = models.TextField(blank=True, default='')
    width = models.CharField(max_length=50, blank=True, default='')
    height = models.CharField(max_length=50, blank=True, default='')
    style = models.TextField(blank=True, default='')

    class Meta:
        abstract = True


class Accordion(AccordionAbstract):
    def get_name_for_id(self):
        return 'ac{}{}'.format(
            self.name.replace(' ', '').lower(),
            self.id
        )

    def __str__(self):
        if self.name:
            return "Acordeon " + self.name
        else:
            return "Acordeon #" + str(self.id)

class SubAccordion(AccordionAbstract):
    acordeon_padre = models.ForeignKey('Accordion', on_delete=models.CASCADE, default=None)

    def get_name_for_id(self):
        return 'sac{}{}_{}'.format(
            self.name.replace(' ', '').lower(),
            self.acordeon_padre.id,
            self.id
        )

    def __str__(self):
        if self.name:
            return "Sub Acordeon " + self.name
        else:
            return "Sub Acordeon #" + str(self.id)
