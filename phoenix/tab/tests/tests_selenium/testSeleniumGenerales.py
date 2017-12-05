from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

## Chequea que la página tab funcione correctamente
class TestSeleniumTab(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSeleniumTab, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumTab, cls).tearDownClass()

    def test_tiene_el_titulo_adecuado(self):
        "Prueba que la página del tab tenga el título adecuado"
        self.selenium.get('%s%s' % (self.live_server_url, '/tab/'))
        self.assertIn("Phoenix Team | Editor", self.selenium.title)

    def test_no_tiene_tab(self):
        "Comprueba que no se muestre ningun tab en la vista"
        self.selenium.get('%s%s' % (self.live_server_url, '/tab/'))
        self.assertTrue(not self.selenium.find_elements_by_css_selector('.nav.nav-tabs'))

