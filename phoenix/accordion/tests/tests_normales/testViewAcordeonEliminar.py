from django.test import TestCase

from accordion.models import Accordion


# Realiza pruebas a la vista encargada de eliminar los acordeones de un usuario
class TestAcordeonEliminar(TestCase):
    def setUp(self):
        self.acordeon_mdl = Accordion.objects.create(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_style="contenido_estilo2",
            width="1232",
            height="9872",
            style="estilo2",
        )

    def test_acordeon_eliminar_funcionando_get(self):
        "Checkea que la vista no de error si se quiere eliminar un acordeon"
        response = self.client.get(
            '/eliminar-acordeon/' + str(self.acordeon_mdl.accordion_id)
        )
        ## 302 = Redireccion
        self.assertEqual(response.status_code, 302)

        self.assertRaises(
            Accordion.DoesNotExist,
            lambda: Accordion.all_objects.get(accordion_id=self.acordeon_mdl.accordion_id),
        )
