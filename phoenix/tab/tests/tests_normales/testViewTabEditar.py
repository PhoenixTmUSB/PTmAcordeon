from django.test import TestCase
from tab.forms import TabForm
from tab.models import Tab, TabContainer


# Realiza pruebas a la vista encargada de editar los tab de un usuario
class TestTabEdit(TestCase):
    def setUp(self):
        self.tab_container = TabContainer.objects.create(
            name="container",
            children_amount=1,
        )
        self.tab_mdl= Tab.objects.create(
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
            parent = self.tab_container
        )

    def test_tab_editar_funcionando_get(self):
        "Checkea que la vista no de error si se accede normalmente"
        response = self.client.get(
            '/editar-tab/' + str(self.tab_mdl.tab_id)
        )
        self.assertEqual(response.status_code, 200)

    def test_tab_editar_funcionando_post(self):
        "Checkea que la vista edite un tab"

        form = TabForm(None, instance=self.tab_mdl)

        data = {key: form.initial.get(key, '') + '_12' for key in form.initial.keys()}
        data['number_tabs'] = 1

        response = self.client.post(
            '/editar-tab/' + str(self.tab_mdl.tab_id),
            data
        )

        self.assertEqual(response.status_code, 200)

        tab_mdl_bd = Tab.objects.get(title=self.tab_mdl.title + '_12')

        self.assertEqual(self.tab_mdl.title + '_12', tab_mdl_bd.title)
        self.assertEqual(self.tab_mdl.title_style + '_12', tab_mdl_bd.title_style)
        self.assertEqual(self.tab_mdl.content + '_12', tab_mdl_bd.content)
        self.assertEqual(self.tab_mdl.content_color + '_12', tab_mdl_bd.content_color)
        self.assertEqual(self.tab_mdl.content_style + '_12', tab_mdl_bd.content_style)
        self.assertEqual(self.tab_mdl.border_color + '_12', tab_mdl_bd.border_color)
        self.assertEqual(self.tab_mdl.border_style + '_12', tab_mdl_bd.border_style)
        self.assertEqual(self.tab_mdl.border_radius + '_12', tab_mdl_bd.border_radius)
        self.assertEqual(self.tab_mdl.width + '_12', tab_mdl_bd.width)
        self.assertEqual(self.tab_mdl.height + '_12', tab_mdl_bd.height)
        self.assertEqual(self.tab_mdl.style + '_12', tab_mdl_bd.style)

