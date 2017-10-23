from django.test import TestCase

from accordion.forms import AccordionForm
from accordion.models import Accordion


# Realiza pruebas a la vista encargada de editar los acordeones de un usuario
class TestAcordeonEdit(TestCase):
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

    def test_acordeon_editar_funcionando_get(self):
        "Checkea que la vista no de error si se accede normalmente"
        response = self.client.get(
            '/editar-acordeon/' + str(self.acordeon_mdl.accordion_id)
        )
        self.assertEqual(response.status_code, 200)

    def test_acordeon_editar_funcionando_post(self):
        "Checkea que la vista edite un acordeon"

        form = AccordionForm(None, instance=self.acordeon_mdl)

        data = {key: form.initial.get(key, '') + '_12' for key in form.initial.keys()}
        data['panels'] = 0

        response = self.client.post(
            '/editar-acordeon/' + str(self.acordeon_mdl.accordion_id),
            data
        )

        self.assertEqual(response.status_code, 200)

        acordeon_mdl_bd = Accordion.all_objects.get(title=self.acordeon_mdl.title + '_12')

        self.assertEqual(self.acordeon_mdl.title_style + '_12', acordeon_mdl_bd.title_style)
        self.assertEqual(self.acordeon_mdl.content + '_12', acordeon_mdl_bd.content)
        self.assertEqual(self.acordeon_mdl.content_style + '_12', acordeon_mdl_bd.content_style)
        self.assertEqual(self.acordeon_mdl.width + '_12', acordeon_mdl_bd.width)
        self.assertEqual(self.acordeon_mdl.height + '_12', acordeon_mdl_bd.height)
        self.assertEqual(self.acordeon_mdl.style + '_12', acordeon_mdl_bd.style)
