import uuid
from django.db import models
from accordion.models import PatronAbstract


class Minesweep(PatronAbstract):
    SIDE_CHOICES = (
        ('top', 'arriba'),
        ('bottom', 'abajo'),
        ('right', 'derecha'),
        ('left', 'izquierda'),
    )
    tooltip_side = models.CharField(
        u'Lado del tootlip',
        max_length=6,
        choices=SIDE_CHOICES,
        default='arriba'
    )
    minesweep_id = models.UUIDField(
        u'Id del minesweep',
        default=uuid.uuid4,
        editable=False
    )
    tooltip = models.TextField(
        u'Información del tooltip',
        blank=True,
        null=True
    )
    tooltip_style = models.TextField(
        u'Estilos del tooltip',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.minesweep_id)
