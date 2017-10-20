from django.test import TestCase


# Realiza pruebas a la vista encargada de renderizar el acordeon al usuario
class TestAcordeonView(TestCase):
    def test_acordeon_funcionando(self):
        response = self.client.get('/acordeon/')
        self.assertEqual(response.status_code, 200)
