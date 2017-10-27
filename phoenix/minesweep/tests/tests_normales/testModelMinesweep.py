# Realiza pruebas enfocadas en el modelo Minesweep
from django.test import TestCase
from minesweep.models import Minesweep


class TestMinesweep(TestCase):
    def setUp(self):
        # Minesweep.objects.create()
        pass

    def test_se_puede_crear_minesweep(self):
        """Modelo Minesweep Existe"""
        minesweep_mdl = Minesweep()
        self.assertTrue(isinstance(minesweep_mdl, Minesweep))

    def test_crear_un_minesweep_en_bd(self):
        """Modelo Minesweep se puede guardar en la bd con todos los campos"""
        minesweep_mdl = Minesweep(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            width="123",
            height="987",
        )
        minesweep_mdl.save()

        minesweep_mdl2 = Minesweep.objects.get(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            width="123",
            height="987",
        )

        self.assertEqual(minesweep_mdl.tooltip, minesweep_mdl2.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl2.tooltip_style)
        self.assertEqual(minesweep_mdl.content, minesweep_mdl2.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl2.content_style)
        self.assertEqual(minesweep_mdl.width, minesweep_mdl2.width)
        self.assertEqual(minesweep_mdl.height, minesweep_mdl2.height)

    def test_crear_dos_minesweep_bd(self):
        """Se pueden crear más de un minesweep"""
        minesweep_mdl1 = Minesweep(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            width="123",
            height="987",
        )
        minesweep_mdl1.save()

        minesweep_mdl1_bd = Minesweep.objects.get(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            width="123",
            height="987",
        )

        self.assertEqual(minesweep_mdl1.tooltip, minesweep_mdl1_bd.tooltip)
        self.assertEqual(minesweep_mdl1.tooltip_style, minesweep_mdl1_bd.tooltip_style)
        self.assertEqual(minesweep_mdl1.content, minesweep_mdl1_bd.content)
        self.assertEqual(minesweep_mdl1.content_style, minesweep_mdl1_bd.content_style)
        self.assertEqual(minesweep_mdl1.width, minesweep_mdl1_bd.width)
        self.assertEqual(minesweep_mdl1.height, minesweep_mdl1_bd.height)

        minesweep_mdl2 = Minesweep(
            tooltip="tooltip2",
            tooltip_style="tooltip_style2",
            content="content2",
            content_style="content_style2",
            width="1232",
            height="9872",
        )
        minesweep_mdl2.save()

        minesweep_mdl2_bd = Minesweep.objects.get(
            tooltip="tooltip2",
            tooltip_style="tooltip_style2",
            content="content2",
            content_style="content_style2",
            width="1232",
            height="9872",
        )

        self.assertEqual(minesweep_mdl2.tooltip, minesweep_mdl2_bd.tooltip)
        self.assertEqual(minesweep_mdl2.tooltip_style, minesweep_mdl2_bd.tooltip_style)
        self.assertEqual(minesweep_mdl2.content, minesweep_mdl2_bd.content)
        self.assertEqual(minesweep_mdl2.content_style, minesweep_mdl2_bd.content_style)
        self.assertEqual(minesweep_mdl2.width, minesweep_mdl2_bd.width)
        self.assertEqual(minesweep_mdl2.height, minesweep_mdl2_bd.height)