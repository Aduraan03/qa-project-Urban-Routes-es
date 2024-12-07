import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_page import UrbanRoutesPage
from retrieve_phone_code import retrieve_phone_code
import data


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--start-maximized")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    """def test_complete_taxi_request(self):
        self.page.set_route(data.address_from, data.address_to)
        self.page.request_taxi()
        self.page.select_comfort_tariff()
        self.page.open_phone_modal()
        self.page.fill_phone_number(data.phone_number)
        self.page.click_next_button()
        confirmation_code = retrieve_phone_code(self.driver)
        self.page.enter_confirmation_code(confirmation_code)
        self.page.click_payment_method_button()
        self.page.click_add_card_option()
        self.page.fill_card_number(data.card_number)
        self.page.fill_cvv(data.card_code)
        self.page.click_add_card_button()
        self.page.close_modal()
        self.page.write_message_for_driver(data.message_for_driver)
        self.page.toggle_blanket_tissues()
        self.page.increment_ice_cream_count(2)
        self.page.click_pedir_taxi()
        driver_info = self.page.wait_for_driver_info()
        assert driver_info != "", "La información del conductor no está disponible."
        print(f"Información del conductor: {driver_info}")"""
    #Separe las pruebas


    #Definir ruta y pedir taxi
    def test_set_route(self):
        self.page.set_route(data.address_from, data.address_to)
        assert self.page.verify_route_set(), f"La ruta no se configuró correctamente."

    def test_request_taxi(self):
        self.page.request_taxi()
        assert self.page.verify_request_taxi(), f"No se pudo solicitar el taxi."
    #seleccionar comfort taxi
    def test_select_comfort_taxi(self):
        self.page.select_comfort_tariff()
        assert self.page.verify_select_comfort_tariff(), "No se selecciono comfort taxi"
    #agregar numero de telefono
    def test_set_phone_number(self):
        self.page.open_phone_modal()
        self.page.fill_phone_number(data.phone_number)
        self.page.click_next_button()
        confirmation_code = retrieve_phone_code(self.driver)
        self.page.enter_confirmation_code(confirmation_code)
        assert self.page.verify_set_phone_number(), "No se agrego el número de telefono"

    #Agregar tarjeta
    def test_add_card(self):
        self.page.click_payment_method_button()
        self.page.click_add_card_option()
        self.page.fill_card_number(data.card_number)
        self.page.fill_cvv(data.card_code)
        self.page.click_add_card_button()
        self.page.close_modal()
        assert self.page.verify_add_card(), "No se agrego correctamente la tarjeta"

    #Escribir mensaje al conductor
    def test_write_message(self):
        self.page.write_message_for_driver(data.message_for_driver)
        assert self.page.verify_write_message(), "El mensaje al conductor no se pudo escribir, mandar"

    # Prueba que verifica que se pueda solicitó una manta
    def test_blanket(self):
        self.page.toggle_blanket_tissues()
        assert self.page.verify_blanket(), "No se pudo agregar manta y pañuelos"
    # Prueba que verifica que se añadieron helados
    def test_add_icecream(self):
        self.page.increment_ice_cream_count(2)
        assert self.page.verify_icecream(), "No se pudo agregar dos helados"
    # Prueba que verifica la búsqueda de un conductor
    def test_find_driver(self):
        self.page.click_pedir_taxi()
        assert self.page.verify_find_taxi(), "El taxi no fue pedido correctamente"
    # Prueba que verifica que la información del conductor se muestra correctamente después de la búsqueda (Esta prueba es opcional)
    def test_wait_driver_information(self):
        driver_info = self.page.wait_for_driver_info()
        assert driver_info != "", "La información del conductor no está disponible."
        print(f"Información del conductor: {driver_info}")
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
