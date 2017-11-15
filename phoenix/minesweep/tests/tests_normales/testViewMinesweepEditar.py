from django.test import TestCase
from minesweep.forms import MinesweepForm
from minesweep.models import Minesweep


# Realiza pruebas a la vista encargada de editar los minesweep de un usuario
class TestMinesweepEdit(TestCase):
    def setUp(self):
        self.minesweep_mdl = Minesweep.objects.create(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            content_color="content_color",
            border_style = 'border_style',
            border_color = 'border_color',
            width="123",
            height="987",
            tooltip_side='bottom',
            style = "",
        )

    def test_minesweep_editar_funcionando_get(self):
        "Checkea que la vista no de error si se accede normalmente"
        response = self.client.get(
            '/editar-minesweep/' + str(self.minesweep_mdl.minesweep_id)
        )
        self.assertEqual(response.status_code, 200)

    def test_minesweep_editar_funcionando_post(self):
        "Checkea que la vista edite un minesweep"

        form = MinesweepForm(None, instance=self.minesweep_mdl)

        data = {}
        for key in form.initial.keys():
            value_key = form.initial.get(key, '')
            data[key] = value_key + '_12'
        data['tooltip_side'] = 'right'

        response = self.client.post(
            '/editar-minesweep/' + str(self.minesweep_mdl.minesweep_id),
            data
        )

        self.assertEqual(response.status_code, 200)

        minesweep_mdl_bd = Minesweep.objects.get(tooltip=self.minesweep_mdl.tooltip + '_12')

        self.assertEqual(self.minesweep_mdl.tooltip + '_12', minesweep_mdl_bd.tooltip)
        self.assertEqual(self.minesweep_mdl.tooltip_style + '_12', minesweep_mdl_bd.tooltip_style)
        self.assertEqual(self.minesweep_mdl.content + '_12', minesweep_mdl_bd.content)
        self.assertEqual(self.minesweep_mdl.content_style + '_12', minesweep_mdl_bd.content_style)
        self.assertEqual(self.minesweep_mdl.width + '_12', minesweep_mdl_bd.width)
        self.assertEqual(self.minesweep_mdl.height + '_12', minesweep_mdl_bd.height)
        self.assertEqual('right', minesweep_mdl_bd.tooltip_side)
