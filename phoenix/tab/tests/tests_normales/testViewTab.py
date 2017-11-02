from django.test import TestCase

# Realiza pruebas a la vista encargada de renderizar los tab de un usuario
class TestTabView(TestCase):
    def test_tab_funcionando(self):
        response = self.client.get('/tab/')
        self.assertEqual(response.status_code, 200)
