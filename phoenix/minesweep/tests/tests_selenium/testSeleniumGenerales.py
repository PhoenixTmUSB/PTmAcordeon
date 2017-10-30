from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

## Chequea que la página minesweep funcione correctamente
class TestSeleniumMinesweep(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSeleniumMinesweep, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumMinesweep, cls).tearDownClass()

    def test_tiene_el_titulo_adecuado(self):
        "Prueba que la página del minesweep tenga el título adecuado"
        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        self.assertIn("Phoenix Team | Editor", self.selenium.title)

    def test_no_tiene_minesweep(self):
        "Comprueba que no se muestre ningun minesweep en la vista"
        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        self.assertTrue(not self.selenium.find_elements_by_css_selector('.panel.tooltipster'))

