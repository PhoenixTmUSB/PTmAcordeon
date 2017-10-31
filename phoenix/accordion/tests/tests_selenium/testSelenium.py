from time import sleep

import selenium
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from accordion.models import Accordion


class TestSeleniumHome(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSeleniumHome, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumHome, cls).tearDownClass()

    ## Solo abre el home y chequea que se muestre el título correcto en el navegador
    def test_home_ok(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn("Phoenix Team | Editor", self.selenium.title)


## Chequea que la página acordeon funcione correctamente
class TestSeleniumAcordeon(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSeleniumAcordeon, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumAcordeon, cls).tearDownClass()

    def test_tiene_el_titulo_adecuado(self):
        "Prueba que la página del acordeon tenga el título adecuado"
        self.selenium.get('%s%s' % (self.live_server_url, '/acordeon/'))
        self.assertIn("Phoenix Team | Editor", self.selenium.title)

    def test_no_tiene_acordeon(self):
        "Comprueba que no se muestre ningun acordeon en la vista"
        self.selenium.get('%s%s' % (self.live_server_url, '/acordeon/'))
        with self.assertRaises(selenium.common.exceptions.NoSuchElementException) as cm:
            self.selenium.find_element_by_css_selector(".panel.panel-default")

        self.assertTrue(isinstance(cm.exception, NoSuchElementException))


## Chequea que un usuario pueda iniciar sesión sin problemas

class TestSeleniumUsuarioInicioSesion(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSeleniumUsuarioInicioSesion, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(0)

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

        # Esperamos 4 segundos
        sleep(4)

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

    def criterio_crear_acordeon_con_un_panel(self):
        "Prueba que un usuario pueda crear un acordeon con un solo panel"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-acordeon/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#accordion-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        acordeon_mdl = Accordion(
            title="titulo",
            title_style="color:red",
            content="contenido",
            content_style="color:blue",
            width="100",
            height="50",
            style="color:blue",
        )
        # acordeon_mdl.save()

        form_crear_acordeon = self.selenium.find_element_by_css_selector('form#accordion-create-form')

        form_crear_acordeon.find_element_by_name('title').send_keys(acordeon_mdl.title)
        form_crear_acordeon.find_element_by_name('title_style').send_keys(acordeon_mdl.title_style)
        form_crear_acordeon.find_element_by_name('content').send_keys(acordeon_mdl.content)
        form_crear_acordeon.find_element_by_name('content_style').send_keys(acordeon_mdl.content_style)

        form_crear_acordeon.find_element_by_name('width').clear()
        form_crear_acordeon.find_element_by_name('width').send_keys(acordeon_mdl.width)

        form_crear_acordeon.find_element_by_name('height').clear()
        form_crear_acordeon.find_element_by_name('height').send_keys(acordeon_mdl.height)

        form_crear_acordeon.find_element_by_name('style').send_keys(acordeon_mdl.style)

        # Guardamos la url actual del usuario antes de crear el acordeon
        url_antes_guardar_acordeon = self.selenium.current_url

        form_crear_acordeon.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el acordeon creado
        while url_antes_guardar_acordeon == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/acordeon/'))

        acordeon_mdl_bd = Accordion.all_objects.get(title="titulo")

        self.assertEqual(acordeon_mdl.title, acordeon_mdl_bd.title)
        self.assertEqual(acordeon_mdl.title_style, acordeon_mdl_bd.title_style)
        self.assertEqual(acordeon_mdl.content, acordeon_mdl_bd.content)
        self.assertEqual(acordeon_mdl.content_style, acordeon_mdl_bd.content_style)
        self.assertEqual(acordeon_mdl.width, acordeon_mdl_bd.width)
        self.assertEqual(acordeon_mdl.height, acordeon_mdl_bd.height)
        self.assertEqual(acordeon_mdl.style, acordeon_mdl_bd.style)
        # Faltaría verificar que la preview del acordeon está bien hecha

        self.assertEqual(self.selenium.find_element_by_css_selector(
            'div#accordion-' + str(acordeon_mdl_bd.accordion_id) + ' .panel-title').text, acordeon_mdl_bd.title)

    def agregar_panel_al_acordeon(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-acordeon/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#accordion-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        acordeon_mdl = Accordion(
            title="titulo",
        )

        form_crear_acordeon = self.selenium.find_element_by_css_selector('form#accordion-create-form')

        form_crear_acordeon.find_element_by_name('title').send_keys(acordeon_mdl.title)

        # Guardamos la url actual del usuario antes de crear el acordeon
        url_antes_guardar_acordeon = self.selenium.current_url

        form_crear_acordeon.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el acordeon creado
        while url_antes_guardar_acordeon == self.selenium.current_url:
            sleep(1)

        acordeon_mdl_bd = Accordion.all_objects.get(title="titulo")

        # Guardamos la url que muestra la vista
        current_url_antes_click_editar = self.selenium.current_url

        self.selenium.find_element_by_css_selector('a.edit-panel-button').click()

        # Mientras que no se muestre la vista de editar panel
        while current_url_antes_click_editar == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url,
                         '%s%s' % (self.live_server_url, '/editar-acordeon/' + acordeon_mdl_bd.accordion_id))

        self.selenium.find_element_by_css_selector('input#id_panels').clear()
        self.selenium.find_element_by_css_selector('input#id_panels').send_keys(1)

        # Guardamos la url que muestra la vista de editar panel
        current_url_antes_click_guardar = self.selenium.current_url

        self.selenium.find_element_by_css_selector("button[type='submit']").submit()


        # Mientrasque no se haya redirido a la vista donde se muestra el acordeon editado
        while current_url_antes_click_guardar == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/acordeon/'))


        self.assertEqual(self.selenium.find_element_by_css_selector('div#accordion-'+str(acordeon_mdl_bd.accordion_id) + ' .panel-title').text,acordeon_mdl_bd.title)
