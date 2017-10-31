import uuid
from django.db import models
from accordion.models import PatronAbstract

# Create your models here.
class Tab(PatronAbstract):
    tab_id = models.UUIDField(
        u'Id del tab',
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        u'Titulo del tab',
        blank=True,
        null=True,
        max_length=100,
    )
    title_style = models.TextField(
        u'Estilos del titulo',
        blank=True,
        null=True
    )
    content = models.TextField(
        u'Contenido del tab',
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
        return str(self.tab_id)
