### Realiza pruebas unitarias a los models
## Se asume que el modelo Accordion y SubAccordion existen
import django
from django.db import IntegrityError
from django.test import TestCase

from .models import Accordion, SubAccordion


## Realiza pruebas enfocadas en el modelo Acordeon
class PruebaAcordeon(TestCase):
    def setUp(self):
        # Accordion.objects.create()
        pass

    def test_se_puede_crear_acordeon(self):
        """Modelo Acordeon Existe"""
        acordeon_mdl = Accordion()
        self.assertTrue(isinstance(acordeon_mdl, Accordion))

    def test_crear_un_acordeon_en_bd(self):
        """Modelo Acordeon se puede guardar en la bd con todos los campos"""
        acordeon_mdl = Accordion(
            name="nombre",
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            contet_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo",
        )
        acordeon_mdl.save()

        acordeon_mdl2 = Accordion.objects.get(name="nombre",
                                              title="titulo",
                                              title_style="titulo_estilo",
                                              content="contenido",
                                              contet_style="contenido_estilo",
                                              width="123",
                                              height="987",
                                              style="estilo"
                                              )
        self.assertEqual(acordeon_mdl.name, acordeon_mdl2.name)
        self.assertEqual(acordeon_mdl.title, acordeon_mdl2.title)
        self.assertEqual(acordeon_mdl.title_style, acordeon_mdl2.title_style)
        self.assertEqual(acordeon_mdl.content, acordeon_mdl2.content)
        self.assertEqual(acordeon_mdl.contet_style, acordeon_mdl2.contet_style)
        self.assertEqual(acordeon_mdl.width, acordeon_mdl2.width)
        self.assertEqual(acordeon_mdl.height, acordeon_mdl2.height)
        self.assertEqual(acordeon_mdl.style, acordeon_mdl2.style)

    def test_crear_dos_acordeon_bd(self):
        """Se pueden crear más de un acordeon"""

        acordeon_mdl1 = Accordion(
            name="nombre",
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            contet_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo",
        )
        acordeon_mdl1.save()

        acordeon_mdl1_bd = Accordion.objects.get(name="nombre",
                                                 title="titulo",
                                                 title_style="titulo_estilo",
                                                 content="contenido",
                                                 contet_style="contenido_estilo",
                                                 width="123",
                                                 height="987",
                                                 style="estilo"
                                                 )
        self.assertEqual(acordeon_mdl1.name, acordeon_mdl1_bd.name)
        self.assertEqual(acordeon_mdl1.title, acordeon_mdl1_bd.title)
        self.assertEqual(acordeon_mdl1.title_style, acordeon_mdl1_bd.title_style)
        self.assertEqual(acordeon_mdl1.content, acordeon_mdl1_bd.content)
        self.assertEqual(acordeon_mdl1.contet_style, acordeon_mdl1_bd.contet_style)
        self.assertEqual(acordeon_mdl1.width, acordeon_mdl1_bd.width)
        self.assertEqual(acordeon_mdl1.height, acordeon_mdl1_bd.height)
        self.assertEqual(acordeon_mdl1.style, acordeon_mdl1_bd.style)

        acordeon_mdl2 = Accordion(
            name="nombre2",
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            contet_style="contenido_estilo2",
            width="1232",
            height="9872",
            style="estilo2",
        )
        acordeon_mdl2.save()

        acordeon_mdl2_bd = Accordion.objects.get(name="nombre2",
                                                 title="titulo2",
                                                 title_style="titulo_estilo2",
                                                 content="contenido2",
                                                 contet_style="contenido_estilo2",
                                                 width="1232",
                                                 height="9872",
                                                 style="estilo2"
                                                 )
        self.assertEqual(acordeon_mdl2.name, acordeon_mdl2_bd.name)
        self.assertEqual(acordeon_mdl2.title, acordeon_mdl2_bd.title)
        self.assertEqual(acordeon_mdl2.title_style, acordeon_mdl2_bd.title_style)
        self.assertEqual(acordeon_mdl2.content, acordeon_mdl2_bd.content)
        self.assertEqual(acordeon_mdl2.contet_style, acordeon_mdl2_bd.contet_style)
        self.assertEqual(acordeon_mdl2.width, acordeon_mdl2_bd.width)
        self.assertEqual(acordeon_mdl2.height, acordeon_mdl2_bd.height)
        self.assertEqual(acordeon_mdl2.style, acordeon_mdl2_bd.style)

        todos = Accordion.objects.order_by('name')
        self.assertEqual(todos[0].name, 'nombre')
        self.assertEqual(todos[1].name, 'nombre2')

    def test_create_dos_modelo_acordeon_guardar_bd_dos_campo_name_iguales(self):
        """Modelo Acordeon no se puede guardar en la BD porque ya existe uno con el mismo nombre"""
        acordeon_mdl = Accordion(name="hola")
        acordeon_mdl.save()

        acordeon_mdl2 = Accordion(name="hola")
        with self.assertRaises(django.db.utils.IntegrityError) as cm:
            acordeon_mdl2.save()

        self.assertTrue(isinstance(cm.exception, IntegrityError))

    def test_create_modelo_acordeon_con_sub_acordeon_guardar_bd(self):
        """Un Acordeon puede tener un Sub Acordeon y se puede guardar en la BD"""
        acordeon_mdl_child = SubAccordion(name="hola_ch")
        acordeon_mdl_child.save()

        acordeon_mdl_padre = Accordion(name="hola_pa")
        acordeon_mdl_padre.save()

        acordeon_mdl_padre.sub_accordions.add(acordeon_mdl_child)

        acordeon_mdl_child_padre_bd = Accordion.objects.get(name="hola_pa")
        acordeones_hijos = acordeon_mdl_child_padre_bd.sub_accordions.all()

        acordeon_child_bd = acordeones_hijos[0]

        self.assertTrue(acordeon_child_bd.name == "hola_ch")


## Realiza pruebas enfocadas en el modelo sub acordeon
class PruebaSubAcordeon(TestCase):
    def test_create_modelo_subacordeon_sin_argumentos(self):
        """Modelo Sub Acordeon Existe"""
        subacordeon_mdl = SubAccordion()
        self.assertTrue(isinstance(subacordeon_mdl, SubAccordion))

    def test_create_modelo_subacordeon_guardar_bd_campo_name(self):
        """Modelo Acordeon se puede guardar en la BD"""
        subacordeon_mdl = SubAccordion(name="hola")
        subacordeon_mdl.save()

        acordeon_mdl2 = SubAccordion.objects.get(name="hola")
        self.assertEqual(acordeon_mdl2.name, subacordeon_mdl.name)

    def test_create_modelo_subacordeon_guardar_bd_todos_los_campo(self):
        """Modelo Sub Acordeon se puede guardar en la BD con todos los campos"""
        subacordeon_mdl = SubAccordion(
            name="nombre",
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            contet_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo",
        )
        subacordeon_mdl.save()

        subacordeon_mdl2 = SubAccordion.objects.get(
            name="nombre",
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            contet_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo"
        )
        self.assertEqual(subacordeon_mdl.name, subacordeon_mdl2.name)
        self.assertEqual(subacordeon_mdl.title, subacordeon_mdl2.title)
        self.assertEqual(subacordeon_mdl.title_style, subacordeon_mdl2.title_style)
        self.assertEqual(subacordeon_mdl.content, subacordeon_mdl2.content)
        self.assertEqual(subacordeon_mdl.contet_style, subacordeon_mdl2.contet_style)
        self.assertEqual(subacordeon_mdl.width, subacordeon_mdl2.width)
        self.assertEqual(subacordeon_mdl.height, subacordeon_mdl2.height)
        self.assertEqual(subacordeon_mdl.style, subacordeon_mdl2.style)

    def test_create_dos_modelo_acordeon_guardar_bd_dos_campo_name_iguales(self):
        """Modelo Sub Acordeon no se puede guardar en la BD si existe otro Sub Acordeon con el mismo nombre"""
        subacordeon_mdl = SubAccordion(name="hola")
        subacordeon_mdl.save()

        subacordeon_mdl2 = SubAccordion(name="hola")
        with self.assertRaises(django.db.utils.IntegrityError) as cm:
            subacordeon_mdl2.save()

        self.assertTrue(isinstance(cm.exception, IntegrityError))
