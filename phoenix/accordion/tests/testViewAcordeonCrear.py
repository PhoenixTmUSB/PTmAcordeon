from django.test import TestCase

from accordion.forms import AccordionForm
from accordion.models import Accordion


# Realiza pruebas a la vista encargada de crear acordeones
class TestAcordeonView(TestCase):
    def test_acordeon_crear_funcionando_get(self):
        "Checkea que se pueda acceder a la vista crear acordeon"
        response = self.client.get('/crear-acordeon/')
        self.assertEqual(response.status_code, 400)

    def test_acordeon_crear_funcionando_post(self):
        "Checkea que la vista esté funcionando para crear un acordeon"
        acordeon_mdl = Accordion(
            title="titulo2",
            title_style="titulo_estilo2",
            content="contenido2",
            content_style="contenido_estilo2",
            width="1232",
            height="9872",
            style="estilo2",
        )

        form = AccordionForm(None, instance=acordeon_mdl)

        data = {key: form.initial.get(key, '') for key in form.initial.keys()}
        data['panels'] = 0

        response = self.client.post(
            '/crear-acordeon/',
            data
        )
        self.assertEqual(response.status_code, 200)

        acordeon_mdl_bd = Accordion.all_objects.get(title=acordeon_mdl.title)

        self.assertEqual(acordeon_mdl.title_style, acordeon_mdl_bd.title_style)
        self.assertEqual(acordeon_mdl.content, acordeon_mdl_bd.content)
        self.assertEqual(acordeon_mdl.content_style, acordeon_mdl_bd.content_style)
        self.assertEqual(acordeon_mdl.width, acordeon_mdl_bd.width)
        self.assertEqual(acordeon_mdl.height, acordeon_mdl_bd.height)
        self.assertEqual(acordeon_mdl.style, acordeon_mdl_bd.style)
