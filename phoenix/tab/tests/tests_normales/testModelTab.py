# Realiza pruebas enfocadas en el modelo Tab
from django.test import TestCase
from tab.models import Tab, TabContainer


class TestTab(TestCase):
    def setUp(self):
        # Tab.objects.create()
        pass

    def test_se_puede_crear_tab(self):
        """Modelo Tab Existe"""
        tab_mdl = Tab()
        self.assertTrue(isinstance(tab_mdl, Tab))

    def test_crear_un_tab_en_bd(self):
        """Modelo Tab se puede guardar en la bd con todos los campos"""
        tab_mdl = Tab(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_color = "red",
            content_style="contenido_estilo2",
            border_color = "blue",
            border_style = "border_style",
            border_radius = "2",
            width="1232",
            height="9872",
            style="estilo2",
        )
        tab_mdl.save()

        tab_mdl2 = Tab.objects.get(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_color = "red",
            content_style="contenido_estilo2",
            border_color = "blue",
            border_style = "border_style",
            border_radius = "2",
            width="1232",
            height="9872",
            style="estilo2",
        )

        self.assertEqual(tab_mdl.title, tab_mdl2.title)
        self.assertEqual(tab_mdl.title_style, tab_mdl2.title_style)
        self.assertEqual(tab_mdl.content, tab_mdl2.content)
        self.assertEqual(tab_mdl.content_color, tab_mdl2.content_color)
        self.assertEqual(tab_mdl.content_style, tab_mdl2.content_style)
        self.assertEqual(tab_mdl.border_color, tab_mdl2.border_color)
        self.assertEqual(tab_mdl.border_style, tab_mdl2.border_style)
        self.assertEqual(tab_mdl.border_radius, tab_mdl2.border_radius)
        self.assertEqual(tab_mdl.width, tab_mdl2.width)
        self.assertEqual(tab_mdl.height, tab_mdl2.height)
        self.assertEqual(tab_mdl.style, tab_mdl2.style)

    def test_crear_dos_tab_bd(self):
        """Se pueden crear más de un tab"""

        tab_container_mdl = TabContainer(name="container",children_amount=2)
        tab_container_mdl.save()

        tab_mdl1 = Tab(
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            content_color = "red",
            content_style="contenido_estilo",
            border_color = "blue",
            border_style = "border_style",
            border_radius = "1",
            width="200",
            height="300",
            style="estilo",
            parent = tab_container_mdl,
        )
        tab_mdl1.save()

        tab_mdl1_bd = Tab.objects.get(
            title="titulo",
            title_style="titulo_estilo",
            content="contenido",
            content_color = "red",
            content_style="contenido_estilo",
            border_color = "blue",
            border_style = "border_style",
            border_radius = "1",
            width="200",
            height="300",
            style="estilo",
        )

        self.assertEqual(tab_mdl1.title, tab_mdl1_bd.title)
        self.assertEqual(tab_mdl1.title_style, tab_mdl1_bd.title_style)
        self.assertEqual(tab_mdl1.content, tab_mdl1_bd.content)
        self.assertEqual(tab_mdl1.content_color, tab_mdl1_bd.content_color)
        self.assertEqual(tab_mdl1.content_style, tab_mdl1_bd.content_style)
        self.assertEqual(tab_mdl1.border_color, tab_mdl1_bd.border_color)
        self.assertEqual(tab_mdl1.border_style, tab_mdl1_bd.border_style)
        self.assertEqual(tab_mdl1.border_radius, tab_mdl1_bd.border_radius)
        self.assertEqual(tab_mdl1.width, tab_mdl1_bd.width)
        self.assertEqual(tab_mdl1.height, tab_mdl1_bd.height)
        self.assertEqual(tab_mdl1.style, tab_mdl1_bd.style)

        tab_mdl2 = Tab(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_color = "red2",
            content_style="contenido_estilo2",
            border_color = "blue2",
            border_style = "border_style2",
            border_radius = "2",
            width="2002",
            height="3002",
            style="estilo2",
            parent=tab_container_mdl,
        )
        tab_mdl2.save()

        tab_mdl2_bd = Tab.objects.get(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_color = "red2",
            content_style="contenido_estilo2",
            border_color = "blue2",
            border_style = "border_style2",
            border_radius = "2",
            width="2002",
            height="3002",
            style="estilo2",
        )

        self.assertEqual(tab_mdl2.title, tab_mdl2_bd.title)
        self.assertEqual(tab_mdl2.title_style, tab_mdl2_bd.title_style)
        self.assertEqual(tab_mdl2.content, tab_mdl2_bd.content)
        self.assertEqual(tab_mdl2.content_color, tab_mdl2_bd.content_color)
        self.assertEqual(tab_mdl2.content_style, tab_mdl2_bd.content_style)
        self.assertEqual(tab_mdl2.border_color, tab_mdl2_bd.border_color)
        self.assertEqual(tab_mdl2.border_style, tab_mdl2_bd.border_style)
        self.assertEqual(tab_mdl2.border_radius, tab_mdl2_bd.border_radius)
        self.assertEqual(tab_mdl2.width, tab_mdl2_bd.width)
        self.assertEqual(tab_mdl2.height, tab_mdl2_bd.height)
        self.assertEqual(tab_mdl2.style, tab_mdl2_bd.style)

        # Chequeamos que las tabs se hayan asignado correctamente al tab container
        tabs = Tab.objects.filter(parent=tab_container_mdl).order_by('border_radius')
        self.assertEqual(tab_mdl1_bd.tab_id, tabs[0].tab_id)
        self.assertEqual(tab_mdl2_bd.tab_id, tabs[1].tab_id)

