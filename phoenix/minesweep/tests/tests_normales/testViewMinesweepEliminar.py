from django.test import TestCase
from minesweep.models import Minesweep


# Realiza pruebas a la vista encargada de eliminar los minesweeps de un usuario
class TestMinesweepEliminar(TestCase):
    def setUp(self):
        self.minesweep_mdl = Minesweep.objects.create(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="content",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )

    def test_minesweep_eliminar_funcionando_get(self):
        "Checkea que la vista no de error si se quiere eliminar un minesweep"
        response = self.client.get(
            '/eliminar-minesweep/' + str(self.minesweep_mdl.minesweep_id)
        )
        ## 302 = Redireccion
        self.assertEqual(response.status_code, 302)

        self.assertRaises(
            Minesweep.DoesNotExist,
            lambda: Minesweep.objects.get(minesweep_id=self.minesweep_mdl.minesweep_id),
        )
