import uuid
from django.db import models
from accordion.models import PatronAbstract

# Create your models here.
class TabContainer(models.Model):
    name = models.CharField(
        u'Nombre del container',
        max_length=100
    )
    children = models.IntegerField(
        default=0
    )

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
    order = models.IntegerField(
        default=0
    )

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.tab_id)
