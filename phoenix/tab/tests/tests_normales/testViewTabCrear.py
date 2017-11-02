from django.test import TestCase
from tab.models import Tab, TabContainer
from tab.forms import TabForm


# Realiza pruebas a la vista encargada de crear los tabs

class TesTabView(TestCase):
    def test_tab_crear_funcionando_get(self):
        "Checkea que se pueda acceder a la vista crear un tab"
        response = self.client.get('/crear-tab/')
        self.assertEqual(response.status_code, 400)

    def test_tab_crear_funcionando_post(self):
        "Checkea que la vista esté funcionando para crear un tab"

        tab_mdl = Tab(
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

        form = TabForm(None, instance=tab_mdl)

        data = {key: form.initial.get(key, '') for key in form.initial.keys()}
        data['number_tabs'] = 1

        response = self.client.post(
            '/crear-tab/',
            data
        )
        self.assertEqual(response.status_code, 200)

        tab_mdl_bd = Tab.objects.get(title=tab_mdl.title)
        
        self.assertEqual(tab_mdl.title, tab_mdl_bd.title)
        self.assertEqual(tab_mdl.title_style, tab_mdl_bd.title_style)
        self.assertEqual(tab_mdl.content, tab_mdl_bd.content)
        self.assertEqual(tab_mdl.content_color, tab_mdl_bd.content_color)
        self.assertEqual(tab_mdl.content_style, tab_mdl_bd.content_style)
        self.assertEqual(tab_mdl.border_color, tab_mdl_bd.border_color)
        self.assertEqual(tab_mdl.border_style, tab_mdl_bd.border_style)
        self.assertEqual(tab_mdl.border_radius, tab_mdl_bd.border_radius)
        self.assertEqual(tab_mdl.width, tab_mdl_bd.width)
        self.assertEqual(tab_mdl.height, tab_mdl_bd.height)
        self.assertEqual(tab_mdl.style, tab_mdl_bd.style)

        # Se le estableció un container
        self.assertIsNotNone(tab_mdl_bd.parent)

        # El container existe
        self.assertTrue(TabContainer.objects.filter(
            children_amount=1,
            name = tab_mdl_bd.parent.name,
            id=tab_mdl_bd.parent.id
        ).exists())
