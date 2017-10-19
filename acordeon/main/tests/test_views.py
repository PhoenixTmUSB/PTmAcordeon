# Realiza pruebas unitarias a los models
# Se asume que el modelo Accordion y SubAccordion existen
from django.test import TestCase


# Realiza pruebas enfocadas en el modelo Acordeon
class TestIndexView(TestCase):
    def test_index_funcionando(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestAcordeonView(TestCase):
    def test_acordeon_funcionando(self):
        response = self.client.get('/acordeon/')
        self.assertEqual(response.status_code, 200)
