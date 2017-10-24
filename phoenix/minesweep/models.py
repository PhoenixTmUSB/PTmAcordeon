import uuid;
from django.db import models

# Create your models here.

class Minesweep(models.Model):
    minesweep_id = models.UUIDField(
        u'Id del minesweep',
        default=uuid.uuid4,
        editable = False
    )
    tooltip = models.TextField(
        u'Información del tooltip',
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
        default='50'
    )
    height = models.CharField(
        u'Alto (px)',
        max_length=50,
        blank=True,
        null=True,
        default='30'
    )

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.minesweep_id)
