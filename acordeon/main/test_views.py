### Realiza pruebas unitarias a los models
## Se asume que el modelo Accordion y SubAccordion existen
from django.test import TestCase


## Realiza pruebas enfocadas en el modelo Acordeon
class PruebaIndexView(TestCase):
    def test_index_funcionando(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class PruebaAcordeonView(TestCase):
    def test_acordeon_funcionando(self):
        response = self.client.get('/acordeon/')
        # a = open('asd.html','wb')
        # a.write(response.content)
        # a.close()
        self.assertEqual(response.status_code, 200)
