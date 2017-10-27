from django.test import TestCase

# Realiza pruebas a la vista encargada de renderizar los minesweep de un usuario
class TestMinesweepView(TestCase):
    def test_minesweep_funcionando(self):
        response = self.client.get('/minesweep/')
        self.assertEqual(response.status_code, 200)
