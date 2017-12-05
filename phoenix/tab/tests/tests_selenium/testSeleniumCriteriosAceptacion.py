from selenium.webdriver.support.ui import Select
from time import sleep
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from tab.models import Tab, TabContainer


class TestSeleniumCriteriosAceptacion(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestSeleniumCriteriosAceptacion, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumCriteriosAceptacion, cls).tearDownClass()

    def test_criterio_crear_un_tab(self):
        "Prueba que un usuario pueda crear un tab"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-tab/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#tab-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal


        ## Falta N Tabs
        n_tabs = 1
        tab_mdl = Tab(
            title="Titulo",
            title_style="color:red",
            content="Contenido Tab",
            content_color = "red",
            content_style="background-color:blue",
            border_style = "dotted",
            border_color = "blue",
            border_radius = "3",
            style="color:green", ## Extra CSS
        )

        form_crear_tab = self.selenium.find_element_by_css_selector('form#tab-create-form')

        form_crear_tab.find_element_by_name('title').send_keys(tab_mdl.title)
        form_crear_tab.find_element_by_name('title_style').send_keys(tab_mdl.title_style)
        form_crear_tab.find_element_by_name('content').send_keys(tab_mdl.content)
        form_crear_tab.find_element_by_name('content_color').send_keys(tab_mdl.content_color)
        form_crear_tab.find_element_by_name('content_style').send_keys(tab_mdl.content_style)
        form_crear_tab.find_element_by_name('border_color').send_keys(tab_mdl.border_color)
        form_crear_tab.find_element_by_name('border_style').send_keys(tab_mdl.border_style)
        form_crear_tab.find_element_by_name('border_radius').send_keys(tab_mdl.border_radius)
        form_crear_tab.find_element_by_name('style').send_keys(tab_mdl.style)

        form_crear_tab.find_element_by_name('number_tabs').clear()
        form_crear_tab.find_element_by_name('number_tabs').send_keys(n_tabs)


        # Guardamos la url actual del usuario antes de crear el tab
        url_antes_guardar_tab = self.selenium.current_url

        form_crear_tab.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el tab creado
        while url_antes_guardar_tab == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/tab/'))

        tab_mdl_bd = Tab.objects.get(title="Titulo")

        self.assertEqual(tab_mdl.title, tab_mdl_bd.title)
        self.assertEqual(tab_mdl.title_style, tab_mdl_bd.title_style)
        self.assertEqual(tab_mdl.content, tab_mdl_bd.content)
        self.assertEqual(tab_mdl.content_color, tab_mdl_bd.content_color)
        self.assertEqual(tab_mdl.content_style, tab_mdl_bd.content_style)
        self.assertEqual(tab_mdl.border_color, tab_mdl_bd.border_color)
        self.assertEqual(tab_mdl.border_style, tab_mdl_bd.border_style)
        self.assertEqual(int(tab_mdl.border_radius), int(tab_mdl_bd.border_radius))
        self.assertEqual(tab_mdl.style, tab_mdl_bd.style)

        # Se le estableció un container
        self.assertIsNotNone(tab_mdl_bd.parent)

        # El container existe
        self.assertTrue(TabContainer.objects.filter(
            children_amount=n_tabs,
            name = tab_mdl_bd.parent.name,
            id=tab_mdl_bd.parent.id
        ).exists())

        # Faltaría verificar que la preview del tab está bien hecha

        tabs_elem = self.selenium.find_element_by_css_selector(".nav.nav-tabs")

        list_tabs = tabs_elem.find_elements_by_css_selector("li")
        self.assertEqual(len(list_tabs),n_tabs)

    def test_criterio_crear_tres_tabs(self):
        "Prueba que un usuario pueda crear tres tab"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-tab/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#tab-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal


        ## Falta N Tabs
        n_tabs = 3
        tab_mdl = Tab(
            title="Titulo",
            title_style="color:red",
            content="Contenido Tab",
            content_color = "red",
            content_style="background-color:blue",
            border_style = "dotted",
            border_color = "blue",
            border_radius = "3",
            style="color:green", ## Extra CSS
        )

        form_crear_tab = self.selenium.find_element_by_css_selector('form#tab-create-form')

        form_crear_tab.find_element_by_name('title').send_keys(tab_mdl.title)
        form_crear_tab.find_element_by_name('title_style').send_keys(tab_mdl.title_style)
        form_crear_tab.find_element_by_name('content').send_keys(tab_mdl.content)
        form_crear_tab.find_element_by_name('content_color').send_keys(tab_mdl.content_color)
        form_crear_tab.find_element_by_name('content_style').send_keys(tab_mdl.content_style)
        form_crear_tab.find_element_by_name('border_color').send_keys(tab_mdl.border_color)
        form_crear_tab.find_element_by_name('border_style').send_keys(tab_mdl.border_style)
        form_crear_tab.find_element_by_name('border_radius').send_keys(tab_mdl.border_radius)
        form_crear_tab.find_element_by_name('style').send_keys(tab_mdl.style)

        form_crear_tab.find_element_by_name('number_tabs').clear()
        form_crear_tab.find_element_by_name('number_tabs').send_keys(n_tabs)


        # Guardamos la url actual del usuario antes de crear el tab
        url_antes_guardar_tab = self.selenium.current_url

        form_crear_tab.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el tab creado
        while url_antes_guardar_tab == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/tab/'))

        # regresa todos los tabs con dicho titulo, n_tabs
        tab_mdl_bd = Tab.objects.filter(title="Titulo")
        self.assertTrue(n_tabs,len(tab_mdl_bd))

        tab_mdl_bd = tab_mdl_bd[0]

        self.assertEqual(tab_mdl.title, tab_mdl_bd.title)
        self.assertEqual(tab_mdl.title_style, tab_mdl_bd.title_style)
        self.assertEqual(tab_mdl.content, tab_mdl_bd.content)
        self.assertEqual(tab_mdl.content_color, tab_mdl_bd.content_color)
        self.assertEqual(tab_mdl.content_style, tab_mdl_bd.content_style)
        self.assertEqual(tab_mdl.border_color, tab_mdl_bd.border_color)
        self.assertEqual(tab_mdl.border_style, tab_mdl_bd.border_style)
        self.assertEqual(int(tab_mdl.border_radius), int(tab_mdl_bd.border_radius))
        self.assertEqual(tab_mdl.style, tab_mdl_bd.style)

        # Se le estableció un container
        self.assertIsNotNone(tab_mdl_bd.parent)

        # El container existe
        self.assertTrue(TabContainer.objects.filter(
            children_amount=n_tabs,
            name = tab_mdl_bd.parent.name,
            id=tab_mdl_bd.parent.id
        ).exists())

        # Faltaría verificar que la preview del tab está bien hecha

        tabs_elem = self.selenium.find_element_by_css_selector(".nav.nav-tabs")

        list_tabs = tabs_elem.find_elements_by_css_selector("li")
        self.assertEqual(len(list_tabs),n_tabs)
