from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from minesweep.models import Minesweep

class TestSeleniumCriteriosAceptacion(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestSeleniumCriteriosAceptacion, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(0)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumCriteriosAceptacion, cls).tearDownClass()

    def test_criterio_crear_objeto_imagen(self):
        "Prueba que un usuario pueda crear un objeto-imagen del minesweep"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-minesweep/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        minesweep_mdl = Minesweep(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        # minesweep_mdl.save()

        form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')

        form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)

        select =  Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        select.select_by_value(minesweep_mdl.tooltip_side)

        form_crear_minesweep.find_element_by_name('width').clear()
        form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)

        form_crear_minesweep.find_element_by_name('height').clear()
        form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)

        # Guardamos la url actual del usuario antes de crear el minesweep
        url_antes_guardar_minesweep = self.selenium.current_url

        form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        while url_antes_guardar_minesweep == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))

        minesweep_mdl_bd = Minesweep.objects.get(tooltip="tooltip")

        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

        # Faltaría verificar que la preview del minesweep está bien hecha

        self.assertEqual(self.selenium.find_element_by_css_selector(
            'div[data-tooltip-content="#minesweep-' + str(minesweep_mdl_bd.minesweep_id) + '"] img').get_attribute('src'), self.live_server_url + '/static/img/objeto1.png')

    def test_criterio_cambiar_imagen_objeto(self):
        "Prueba que un usuario pueda cambiar la imagen de un objeto del minesweep"
        minesweep_mdl = Minesweep(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='left'
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_editar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.edit-panel-button');

        # Guardamos la url actual del usuario antes de editar el minesweep
        url_antes_de_accion = self.selenium.current_url

        enl_editar.click()  # Click al enlace para editar el objeto

        # Mientrasque no se haya redirido a la vista donde se edita el minesweep
        while url_antes_de_accion == self.selenium.current_url:
            sleep(1) # PEqueña espera a que se cambie de url

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/editar-minesweep/' + str(minesweep_mdl.minesweep_id)))

        elem_content_actual = self.selenium.find_element_by_css_selector('textarea#id_content')

        # Verificamos que el contenido sea el actual del modelo
        self.assertEqual(
            elem_content_actual.text,
            minesweep_mdl.content
        )
        elem_content_actual.clear()
        elem_content_actual.send_keys("<img src='/static/img/objeto2.png'>")

        elem_boton_submit = self.selenium.find_element_by_css_selector('button#minesweep-edit-submit')

        elem_boton_submit.click()
        sleep(2)  #Esperamos que se guarden

        minesweep_mdl_bd = Minesweep.objects.get(tooltip="tooltip")

        # Chequeamos que se hayan hecho los cambios en la base de datos
        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual("<img src='/static/img/objeto2.png'>",       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))

        # Faltaría verificar que la preview del minesweep está bien hecha

        self.assertEqual(self.selenium.find_element_by_css_selector(
            'div[data-tooltip-content="#minesweep-' + str(minesweep_mdl_bd.minesweep_id) + '"] img').get_attribute('src'), self.live_server_url + '/static/img/objeto2.png')

    def test_criterio_eliminar_imagen_objeto(self):
        "Prueba que un usuario pueda eliminar un objeto del minesweep"

        minesweep_mdl = Minesweep(
            tooltip="tooltip",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_eliminar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.delete-panel-button');

        enl_eliminar.click()  # Click al enlace para editar el objeto

        sleep(1) # Esperamos que aparezca el alert

        self.selenium.switch_to_alert().accept()

        sleep(2) # Esperamos que se borre

        # Chequeamos que ya no exista
        self.assertRaises(
            Minesweep.DoesNotExist,
            lambda: Minesweep.objects.get(minesweep_id=minesweep_mdl.minesweep_id),
        )

        # El url debe ser el mismo
        # Donde se muestran los minesweep
        # En este caso no se debería mostrar ninguno
        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/minesweep/'))

        # Chequeamos que no se esté mostrando el minesweep eliminado
        self.assertTrue(not self.selenium.find_elements_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"]'))

    def test_criterio_establecer_contenido_extra(self):
        "Prueba que un usuario pueda establecer el contenido extra de un objeto minesweep"

        self.selenium.get('%s%s' % (self.live_server_url, '/crear-minesweep/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        minesweep_mdl = Minesweep(
            tooltip="Contenido EXTRA",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        # minesweep_mdl.save()

        form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')

        form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)
        select = Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        select.select_by_value(minesweep_mdl.tooltip_side)

        form_crear_minesweep.find_element_by_name('width').clear()
        form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)

        form_crear_minesweep.find_element_by_name('height').clear()
        form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)

        # Guardamos la url actual del usuario antes de crear el minesweep
        url_antes_guardar_minesweep = self.selenium.current_url

        form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        while url_antes_guardar_minesweep == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))

        minesweep_mdl_bd = Minesweep.objects.get(tooltip="Contenido EXTRA")

        self.assertEqual("Contenido EXTRA",       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_cambiar_contenido_extra(self):
        "Prueba que un usuario pueda cambiar el contenido extra minesweep"
        minesweep_mdl = Minesweep(
            tooltip="Contenido EXTRA",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_editar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.edit-panel-button');

        # Guardamos la url actual del usuario antes de editar el minesweep
        url_antes_de_accion = self.selenium.current_url

        enl_editar.click()  # Click al enlace para editar el objeto

        # Mientrasque no se haya redirido a la vista donde se edita el minesweep
        while url_antes_de_accion == self.selenium.current_url:
            sleep(1) # PEqueña espera a que se cambie de url

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/editar-minesweep/' + str(minesweep_mdl.minesweep_id)))

        elem_conten_extra_actual = self.selenium.find_element_by_css_selector('textarea#id_tooltip')

        # Verificamos que el contenido sea el actual del modelo
        self.assertEqual(
            elem_conten_extra_actual.text,
            minesweep_mdl.tooltip
        )
        elem_conten_extra_actual.clear()
        elem_conten_extra_actual.send_keys("Contenido EXTRA NUEVO")

        elem_boton_submit = self.selenium.find_element_by_css_selector('button#minesweep-edit-submit')

        elem_boton_submit.click()
        sleep(2)  #Esperamos que se guarden

        minesweep_mdl_bd = Minesweep.objects.get(tooltip="Contenido EXTRA NUEVO")

        # Chequeamos que se hayan hecho los cambios en la base de datos
        self.assertEqual("Contenido EXTRA NUEVO",       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_establecer_ancho_contenido_extra(self):
        "Verifica que un usuario pueda establecer el ancho del contenido extra"
        pass

    def test_criterio_cambiar_ancho_contenido_extra(self):
        "Verifica que un usuario pueda cambiar el ancho del contenido extra"
        pass

    def test_criterio_establecer_posicion_contenido_extra(self):
        "Verifica que un usuario pueda establecer la posicion del contenido extra"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-minesweep/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        minesweep_mdl = Minesweep(
            tooltip="Contenido EXTRA",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        # minesweep_mdl.save()

        form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')

        form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)
        select = Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        select.select_by_value('bottom')

        form_crear_minesweep.find_element_by_name('width').clear()
        form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)

        form_crear_minesweep.find_element_by_name('height').clear()
        form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)

        # Guardamos la url actual del usuario antes de crear el minesweep
        url_antes_guardar_minesweep = self.selenium.current_url

        form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        while url_antes_guardar_minesweep == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_side="bottom")

        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual("bottom",        minesweep_mdl_bd.tooltip_side)

    def test_criterio_cambiar_posicion_contenido_extra(self):
        "Verifica que un usuario pueda cambiar la posicion del contenido extra"
        minesweep_mdl = Minesweep(
            tooltip="Contenido EXTRA",
            tooltip_style="tooltip_style",
            content="<img src='/static/img/objeto1.png'>",
            content_style="content_style",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_editar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.edit-panel-button');

        # Guardamos la url actual del usuario antes de editar el minesweep
        url_antes_de_accion = self.selenium.current_url

        enl_editar.click()  # Click al enlace para editar el objeto

        # Mientrasque no se haya redirido a la vista donde se edita el minesweep
        while url_antes_de_accion == self.selenium.current_url:
            sleep(1) # PEqueña espera a que se cambie de url

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/editar-minesweep/' + str(minesweep_mdl.minesweep_id)))

        elem_conten_extra_actual = self.selenium.find_element_by_css_selector('select#id_tooltip_side')
        select = Select(elem_conten_extra_actual)

        # Verificamos que el contenido sea el actual del modelo
        self.assertEqual(
            select.first_selected_option.get_attribute('value'),
            minesweep_mdl.tooltip_side
        )
        select.select_by_value('top')


        elem_boton_submit = self.selenium.find_element_by_css_selector('button#minesweep-edit-submit')

        elem_boton_submit.click()
        sleep(2)  #Esperamos que se guarden

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_side="top")

        # Chequeamos que se hayan hecho los cambios en la base de datos
        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual("top",        minesweep_mdl_bd.tooltip_side)

    def test_criterio_establecer_color_contenido_extra(self):
        "Verifica que un usuario pueda establecer el color del contenido extra"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-minesweep/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        minesweep_mdl = Minesweep(
            tooltip="Contenido EXTRA",
            tooltip_style = "color:red;",
            content="<img src='/static/img/objeto1.png'>",
            content_style="color:red;",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        # minesweep_mdl.save()

        form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')

        form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)
        select = Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        select.select_by_value(minesweep_mdl.tooltip_side)

        form_crear_minesweep.find_element_by_name('width').clear()
        form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)

        form_crear_minesweep.find_element_by_name('height').clear()
        form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)

        # Guardamos la url actual del usuario antes de crear el minesweep
        url_antes_guardar_minesweep = self.selenium.current_url

        form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        while url_antes_guardar_minesweep == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_style="color:red;")

        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_cambiar_color_contenido_extra(self):
        "Verifica que un usuario pueda cambiar el color del contenido extra"
        minesweep_mdl = Minesweep(
            tooltip="Contenido EXTRA",
            tooltip_style="color:red;",
            content="<img src='/static/img/objeto1.png'>",
            content_style="color:red;",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_editar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.edit-panel-button');

        # Guardamos la url actual del usuario antes de editar el minesweep
        url_antes_de_accion = self.selenium.current_url

        enl_editar.click()  # Click al enlace para editar el objeto

        # Mientrasque no se haya redirido a la vista donde se edita el minesweep
        while url_antes_de_accion == self.selenium.current_url:
            sleep(1) # PEqueña espera a que se cambie de url

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/editar-minesweep/' + str(minesweep_mdl.minesweep_id)))

        elem_conten_style_extra_actual = self.selenium.find_element_by_css_selector('textarea#id_tooltip_style')

        # Verificamos que el contenido sea el actual del modelo
        self.assertEqual(
            elem_conten_style_extra_actual.text,
            minesweep_mdl.tooltip_style
        )
        elem_conten_style_extra_actual.clear()
        elem_conten_style_extra_actual.send_keys("color:yellow;")

        elem_boton_submit = self.selenium.find_element_by_css_selector('button#minesweep-edit-submit')

        elem_boton_submit.click()
        sleep(2)  #Esperamos que se guarden

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_style="color:yellow;")

        # Chequeamos que se hayan hecho los cambios en la base de datos
        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual("color:yellow;",             minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_insertar_imagen_contenido_extra(self):
        "Verifica que un usuario pueda insertar una imagen en el contenido extra"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-minesweep/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        minesweep_mdl = Minesweep(
            tooltip="<img src='/static/img/objeto2.png'>",
            tooltip_style = "color:red;",
            content="<img src='/static/img/objeto1.png'>",
            content_style="color:red;",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        # minesweep_mdl.save()

        form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')

        form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)
        select = Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        select.select_by_value(minesweep_mdl.tooltip_side)

        form_crear_minesweep.find_element_by_name('width').clear()
        form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)

        form_crear_minesweep.find_element_by_name('height').clear()
        form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)

        # Guardamos la url actual del usuario antes de crear el minesweep
        url_antes_guardar_minesweep = self.selenium.current_url

        form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        while url_antes_guardar_minesweep == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_style="color:red;")

        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_cambiar_imagen_insertada_contenido_extra(self):
        "Verifica que un usuario pueda cambiar una imagen en el contenido extra"
        minesweep_mdl = Minesweep(
            tooltip="<img src='/static/img/objeto1.png'>",
            tooltip_style="color:red;",
            content="<img src='/static/img/objeto1.png'>",
            content_style="color:red;",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_editar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.edit-panel-button');

        # Guardamos la url actual del usuario antes de editar el minesweep
        url_antes_de_accion = self.selenium.current_url

        enl_editar.click()  # Click al enlace para editar el objeto

        # Mientrasque no se haya redirido a la vista donde se edita el minesweep
        while url_antes_de_accion == self.selenium.current_url:
            sleep(1) # PEqueña espera a que se cambie de url

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/editar-minesweep/' + str(minesweep_mdl.minesweep_id)))

        elem_content_extra_actual = self.selenium.find_element_by_css_selector('textarea#id_tooltip')

        # Verificamos que el contenido sea el actual del modelo
        self.assertEqual(
            elem_content_extra_actual.text,
            minesweep_mdl.tooltip
        )
        elem_content_extra_actual.clear()
        elem_content_extra_actual.send_keys("<img src='/static/img/objeto2.png'>")

        elem_boton_submit = self.selenium.find_element_by_css_selector('button#minesweep-edit-submit')

        elem_boton_submit.click()
        sleep(2)  #Esperamos que se guarden

        minesweep_mdl_bd = Minesweep.objects.get(tooltip="<img src='/static/img/objeto2.png'>")

        # Chequeamos que se hayan hecho los cambios en la base de datos
        self.assertEqual("<img src='/static/img/objeto2.png'>",       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style,             minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_eliminar_imagen_insertada_contenido_extra(self):
        "Verifica que un usuario pueda eliminar una imagen en el contenido extra"
        minesweep_mdl = Minesweep(
            tooltip="<img src='/static/img/objeto1.png'>",
            tooltip_style="color:red;",
            content="<img src='/static/img/objeto1.png'>",
            content_style="color:red;",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        minesweep_mdl.save()

        self.selenium.get('%s%s' % (self.live_server_url, '/minesweep/'))
        enl_editar = self.selenium.find_element_by_css_selector('div[data-tooltip-content="#minesweep-' + str(minesweep_mdl.minesweep_id) + '"] a.edit-panel-button');

        # Guardamos la url actual del usuario antes de editar el minesweep
        url_antes_de_accion = self.selenium.current_url

        enl_editar.click()  # Click al enlace para editar el objeto

        # Mientrasque no se haya redirido a la vista donde se edita el minesweep
        while url_antes_de_accion == self.selenium.current_url:
            sleep(1) # PEqueña espera a que se cambie de url

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url,'/editar-minesweep/' + str(minesweep_mdl.minesweep_id)))

        elem_content_extra_actual = self.selenium.find_element_by_css_selector('textarea#id_tooltip')

        # Verificamos que el contenido sea el actual del modelo
        self.assertEqual(
            elem_content_extra_actual.text,
            minesweep_mdl.tooltip
        )
        elem_content_extra_actual.clear()

        elem_boton_submit = self.selenium.find_element_by_css_selector('button#minesweep-edit-submit')

        elem_boton_submit.click()
        sleep(2)  #Esperamos que se guarden

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_style="color:red;")

        # Chequeamos que se hayan hecho los cambios en la base de datos
        self.assertEqual("",       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style,             minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_insertar_vinculo_contenido_extra(self):
        "Verifica que un usuario pueda insertar un vinculo en el contenido extra"
        self.selenium.get('%s%s' % (self.live_server_url, '/crear-minesweep/'))
        enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        enl_modal.click()  # Click al enlace para abrir el modal

        minesweep_mdl = Minesweep(
            tooltip="<a href='http://google.com' target='_blank'><img src='/static/img/objeto2.png'></a>",
            tooltip_style = "color:red;",
            content="<img src='/static/img/objeto1.png'>",
            content_style="color:red;",
            width="123",
            height="987",
            tooltip_side='bottom',
        )
        # minesweep_mdl.save()

        form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')

        form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)
        select = Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        select.select_by_value(minesweep_mdl.tooltip_side)

        form_crear_minesweep.find_element_by_name('width').clear()
        form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)

        form_crear_minesweep.find_element_by_name('height').clear()
        form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)

        # Guardamos la url actual del usuario antes de crear el minesweep
        url_antes_guardar_minesweep = self.selenium.current_url

        form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()

        # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        while url_antes_guardar_minesweep == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))

        minesweep_mdl_bd = Minesweep.objects.get(tooltip_style="color:red;")

        self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)

    def test_criterio_cambiar_vinculo_insertado_contenido_extra(self):
        "Verifica que un usuario pueda cambiar un vinculo en el contenido extra"
        pass

    def test_criterio_eliminar_vinculo_insertado_contenido_extra(self):
        "Verifica que un usuario pueda eliminar un vinculo en el contenido extra"
        pass