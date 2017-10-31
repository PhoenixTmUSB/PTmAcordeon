from django.test import TestCase
from minesweep.models import Minesweep
from minesweep.forms import MinesweepForm


# Realiza pruebas a la vista encargada de crear los minesweeps

class TesMinesweepView(TestCase):
    def test_minesweep_crear_funcionando_get(self):
        "Checkea que se pueda acceder a la vista crear un minesweep"
        response = self.client.get('/crear-minesweep/')
        self.assertEqual(response.status_code, 400)

    def test_minesweep_crear_funcionando_post(self):
        "Checkea que la vista esté funcionando para crear un minesweep"
        minesweep_mdl = Minesweep(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side = 'bottom',
        )

        form = MinesweepForm(None, instance=minesweep_mdl)

        data = {key: form.initial.get(key, '') for key in form.initial.keys()}

        response = self.client.post(
            '/crear-minesweep/',
            data
        )
        self.assertEqual(response.status_code, 200)

        minesweep_mdl_bd = Minesweep.objects.get(tooltip=minesweep_mdl.tooltip)

        self.assertEqual(minesweep_mdl.tooltip, minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content, minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width, minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height, minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side, minesweep_mdl_bd.tooltip_side)
