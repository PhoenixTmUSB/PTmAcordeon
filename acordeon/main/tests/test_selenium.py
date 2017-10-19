# import selenium
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.firefox.webdriver import WebDriver

# from main.models import Accordion


# class TestSeleniumHome(StaticLiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super(TestSeleniumHome, cls).setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(TestSeleniumHome, cls).tearDownClass()

#     ## Solo abre el home y chequea que se muestre el título correcto en el navegador
#     def test_home_ok(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/'))
#         self.assertIn("Phoenix Team | Editor", self.selenium.title)


# ## Chequea que la página acordeon funcione correctamente
# class TestSeleniumAcordeon(StaticLiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super(TestSeleniumAcordeon, cls).setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(50)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(TestSeleniumAcordeon, cls).tearDownClass()

#     def test_tiene_el_titulo_adecuado(self):
#         "Prueba que la página del acordeon tenga el título adecuado"
#         self.selenium.get('%s%s' % (self.live_server_url, '/acordeon/'))
#         self.assertIn("Phoenix Team | Editor", self.selenium.title)

#     def test_no_tiene_acordeon(self):
#         "Comprueba que no se muestre ningun acordeon en la vista"
#         self.selenium.get('%s%s' % (self.live_server_url, '/acordeon/'))
#         with self.assertRaises(selenium.common.exceptions.NoSuchElementException) as cm:
#             self.selenium.find_element_by_css_selector(".panel.panel-default")

#         self.assertTrue(isinstance(cm.exception, NoSuchElementException))

#     def test_se_crean_dos_acordeon_simple(self):
#         acordeon_mdl1 = Accordion(
#             name="nombre acordeon 1",
#             content="Contenido del Acordeon 1",
#             content_style='color:azure;',
#             title="Titulo del Acordeon 1",
#             title_style="color:red;",
#             width='320px',
#             height='480px',
#             style='color:yellow;',
#         )
#         acordeon_mdl1.save()

#         acordeon_mdl2 = Accordion(
#             name="nombre acordeon 2",
#             content="Contenido del Acordeon 2",
#             content_style='color:gray;',
#             title="Titulo del Acordeon 2",
#             title_style="color:black;",
#             width='321px',
#             height='482px',
#             style='color:blue;',
#         )
#         acordeon_mdl2.save()

#         self.selenium.get('%s%s' % (self.live_server_url, '/acordeon/'))

#         elem1 = self.selenium.find_element_by_css_selector(
#             "div.panel-group#accordion div.panel.panel-default div#nombreacordeon1"
#         )

#         elem2 = self.selenium.find_element_by_css_selector(
#             "div.panel-group#accordion div.panel.panel-default div#nombreacordeon2"
#         )
