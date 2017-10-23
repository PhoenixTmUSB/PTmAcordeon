from django.test import TestCase


# Realiza pruebas enfocadas en la vista inicial que ve el usuario
class TestHomeView(TestCase):
    def test_index_funcionando(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
