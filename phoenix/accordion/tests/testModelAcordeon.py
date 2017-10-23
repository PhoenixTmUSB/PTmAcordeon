# Realiza pruebas enfocadas en el modelo Acordeon
from django.test import TestCase

from accordion.models import Accordion


class TestAcordeon(TestCase):
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
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            content_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo",
        )
        acordeon_mdl.save()

        acordeon_mdl2 = Accordion.objects.get(
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            content_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo"
        )

        self.assertEqual(acordeon_mdl.title, acordeon_mdl2.title)
        self.assertEqual(acordeon_mdl.title_style, acordeon_mdl2.title_style)
        self.assertEqual(acordeon_mdl.content, acordeon_mdl2.content)
        self.assertEqual(acordeon_mdl.content_style, acordeon_mdl2.content_style)
        self.assertEqual(acordeon_mdl.width, acordeon_mdl2.width)
        self.assertEqual(acordeon_mdl.height, acordeon_mdl2.height)
        self.assertEqual(acordeon_mdl.style, acordeon_mdl2.style)

    def test_crear_dos_acordeon_bd(self):
        """Se pueden crear más de un acordeon"""
        acordeon_mdl1 = Accordion(
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            content_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo",
        )
        acordeon_mdl1.save()

        acordeon_mdl1_bd = Accordion.objects.get(
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            content_style="contenido_estilo",
            width="123",
            height="987",
            style="estilo"
        )

        self.assertEqual(acordeon_mdl1.title, acordeon_mdl1_bd.title)
        self.assertEqual(acordeon_mdl1.title_style, acordeon_mdl1_bd.title_style)
        self.assertEqual(acordeon_mdl1.content, acordeon_mdl1_bd.content)
        self.assertEqual(acordeon_mdl1.content_style, acordeon_mdl1_bd.content_style)
        self.assertEqual(acordeon_mdl1.width, acordeon_mdl1_bd.width)
        self.assertEqual(acordeon_mdl1.height, acordeon_mdl1_bd.height)
        self.assertEqual(acordeon_mdl1.style, acordeon_mdl1_bd.style)

        acordeon_mdl2 = Accordion(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_style="contenido_estilo2",
            width="1232",
            height="9872",
            style="estilo2",
        )
        acordeon_mdl2.save()

        acordeon_mdl2_bd = Accordion.objects.get(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_style="contenido_estilo2",
            width="1232",
            height="9872",
            style="estilo2"
        )

        self.assertEqual(acordeon_mdl2.title, acordeon_mdl2_bd.title)
        self.assertEqual(acordeon_mdl2.title_style, acordeon_mdl2_bd.title_style)
        self.assertEqual(acordeon_mdl2.content, acordeon_mdl2_bd.content)
        self.assertEqual(acordeon_mdl2.content_style, acordeon_mdl2_bd.content_style)
        self.assertEqual(acordeon_mdl2.width, acordeon_mdl2_bd.width)
        self.assertEqual(acordeon_mdl2.height, acordeon_mdl2_bd.height)
        self.assertEqual(acordeon_mdl2.style, acordeon_mdl2_bd.style)


    def test_create_modelo_acordeon_con_sub_acordeon_guardar_bd(self):
        """Un Acordeon puede tener Sub Acordeones y se pueden guardar en la BD"""

        acordeon_mdl_padre = Accordion(title="hola_pa")
        acordeon_mdl_padre.save()

        acordeon_mdl_child1 = Accordion(title="hola_ch1", parent=acordeon_mdl_padre)
        acordeon_mdl_child1.save()

        acordeon_mdl_child2 = Accordion(title="hola_ch2", parent=acordeon_mdl_padre)
        acordeon_mdl_child2.save()

        acordeones_hijos = Accordion.all_objects.filter(parent=acordeon_mdl_padre).order_by('title')

        self.assertEqual(acordeones_hijos[0].title, "hola_ch1")
        self.assertEqual(acordeones_hijos[1].title, "hola_ch2")
