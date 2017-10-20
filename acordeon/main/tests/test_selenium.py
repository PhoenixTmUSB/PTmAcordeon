from time import sleep

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


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


## Chequea que un usuario pueda iniciar sesión sin problemas
class TestSeleniumUsuarioInicioSesion(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSeleniumUsuarioInicioSesion, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(50)

        cls.user_pass_txt = 'soyunapasssegura'
        cls.user = User.objects.create_user('manuggz', 'manuel@coolkids.com', cls.user_pass_txt)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumUsuarioInicioSesion, cls).tearDownClass()

    def test_iniciar_sesion_sim_problemas(self):
        "Prueba que un usuario registrado pueda iniciar sesión y que la página no lo rediriga a otro url"
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        enl_modal = self.selenium.find_element_by_css_selector("a.link-log-in-modal")
        enl_modal.click()  # Click al enlace para abrir el modal

        form_dom = self.selenium.find_element_by_css_selector("form#login-form")

        input_username = form_dom.find_element_by_css_selector("input#login_username")
        input_username.send_keys(self.user.username)

        input_username = form_dom.find_element_by_css_selector("input#login_password")
        input_username.send_keys(self.user_pass_txt)

        boton_iniciar_sesion = form_dom.find_element_by_css_selector("button[type='submit']")

        mensage_log_in = form_dom.find_element_by_css_selector('span#text-login-msg')

        # Guardamos el mensaje que se muestra al usuario antes de que se cambie por el JS
        mensage_log_in_texto_anterior = mensage_log_in.text

        # Guardamos la url actual del usuario antes de iniciar sesión
        url_antes_log_in = self.selenium.current_url

        # Clickeamos el boton para inicar la sesión
        boton_iniciar_sesion.click()

        # Mientras el JS no cambie el mensaje esperamos
        while mensage_log_in_texto_anterior == mensage_log_in.text:
            sleep(1)

        self.assertEqual(mensage_log_in.text, 'Login OK')

        # Esperamos 10 segundos
        sleep(10)

        # Suponemos que no ocurrió una redirección
        self.assertEqual(url_antes_log_in, self.selenium.current_url)

    def test_iniciar_sesion_usuario_no_existente(self):
        "Prueba que un usuario no existente no pueda iniciar sesión"

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        enl_modal = self.selenium.find_element_by_css_selector("a.link-log-in-modal")
        enl_modal.click()  # Click al enlace para abrir el modal

        form_dom = self.selenium.find_element_by_css_selector("form#login-form")

        input_username = form_dom.find_element_by_css_selector("input#login_username")
        input_username.send_keys('usuarionoexistente')

        input_username = form_dom.find_element_by_css_selector("input#login_password")
        input_username.send_keys(self.user_pass_txt)

        boton_iniciar_sesion = form_dom.find_element_by_css_selector("button[type='submit']")

        mensage_log_in = form_dom.find_element_by_css_selector('span#text-login-msg')

        # Guardamos el mensaje que se muestra al usuario antes de que se cambie por el JS
        mensage_log_in_texto_anterior = mensage_log_in.text

        # Guardamos la url actual del usuario antes de iniciar sesión
        url_antes_log_in = self.selenium.current_url

        # Clickeamos el boton para inicar la sesión
        boton_iniciar_sesion.click()

        # Mientras el JS no cambie el mensaje esperamos
        while mensage_log_in_texto_anterior == mensage_log_in.text:
            sleep(1)

        self.assertEqual(mensage_log_in.text, 'Login error')

    def test_iniciar_sesion_usuario_contra_incorrecta(self):
        "Prueba que un usuario si introduce su contraseña incorrecta no pueda iniciar sesión"
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        enl_modal = self.selenium.find_element_by_css_selector("a.link-log-in-modal")
        enl_modal.click()  # Click al enlace para abrir el modal

        form_dom = self.selenium.find_element_by_css_selector("form#login-form")

        input_username = form_dom.find_element_by_css_selector("input#login_username")
        input_username.send_keys(self.user.username)

        input_username = form_dom.find_element_by_css_selector("input#login_password")
        input_username.send_keys(self.user_pass_txt + 'jeje')

        boton_iniciar_sesion = form_dom.find_element_by_css_selector("button[type='submit']")

        mensage_log_in = form_dom.find_element_by_css_selector('span#text-login-msg')

        # Guardamos el mensaje que se muestra al usuario antes de que se cambie por el JS
        mensage_log_in_texto_anterior = mensage_log_in.text

        # Guardamos la url actual del usuario antes de iniciar sesión
        url_antes_log_in = self.selenium.current_url

        # Clickeamos el boton para inicar la sesión
        boton_iniciar_sesion.click()

        # Mientras el JS no cambie el mensaje esperamos
        while mensage_log_in_texto_anterior == mensage_log_in.text:
            sleep(1)

        self.assertEqual(mensage_log_in.text, 'Login error')
