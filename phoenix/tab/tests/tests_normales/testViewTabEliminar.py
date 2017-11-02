from django.test import TestCase
from tab.models import Tab, TabContainer


# Realiza pruebas a la vista encargada de eliminar los tabs de un usuario
class TestTabEliminar(TestCase):
    def setUp(self):
        self.tab_container = TabContainer.objects.create(
            name = "container",
            children_amount = 1,
        )

        self.tab_mdl = Tab.objects.create(
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

    def test_tab_eliminar_funcionando_get(self):
        "Checkea que la vista no de error si se quiere eliminar un tab"
        response = self.client.get(
            '/eliminar-tab/' + str(self.tab_mdl.tab_id)
        )
        ## 302 = Redireccion
        self.assertEqual(response.status_code, 302)

        self.assertRaises(
            Tab.DoesNotExist,
            lambda: Tab.objects.get(tab_id=self.tab_mdl.tab_id),
        )
