from django.contrib.auth.models import User
from django.db import models


# Abstracción de un proyecto creado por el usuario
# Un proyecto puede contener distintos patrones / solo 1 de cada 1
class Project(models.Model):
    # Usuario creador/Editor del proyecto
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    # Nombre del proyecto
    # Nota: Default solo aplica a filas anteriores al migrate
    name = models.CharField(max_length=50, blank=False, default='proyecto')
    # fecha_creacion = models.
    # fecha_ultima_edicion = models.

    # Acordion que esta editando el usuario
    # Guardará la referencia al acordeon que cree el usuario
    acordion = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="project_acordion")

class AccordionAbstract(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    title = models.CharField(max_length=50, blank=True, default='')
    title_style = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    contet_style = models.TextField(blank=True, default='')
    width = models.CharField(max_length=50, blank=True, default='')
    height = models.CharField(max_length=50, blank=True, default='')
    style = models.TextField(blank=True, default='')

    def get_name_for_id(self):
        "Remueve todos los caracteres especiales dejando [a-z0-9]"
        return ''.join(e.lower() for e in self.name if e.isalnum())

    class Meta:
        abstract = True


class Accordion(AccordionAbstract):
    def get_identificador(self):
        return 'ac{}{}'.format(
            self.get_name_for_id(),
            self.id
        )

    def __str__(self):
        if self.get_name_for_id():
            return "Acordeon " + self.get_name_for_id()
        else:
            return "Acordeon #" + str(self.id)

class SubAccordion(AccordionAbstract):
    acordeon_padre = models.ForeignKey('Accordion', on_delete=models.CASCADE, default=None)

    def get_identificador(self):
        return 'sac{}{}_{}'.format(
            self.get_name_for_id(),
            self.acordeon_padre.id,
            self.id
        )

    def __str__(self):
        if self.get_name_for_id():
            return "Sub Acordeon " + self.get_name_for_id()
        else:
            return "Sub Acordeon #" + str(self.id)
