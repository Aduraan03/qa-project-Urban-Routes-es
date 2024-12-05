import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_page import UrbanRoutesPage
from retrieve_phone_code import retrieve_phone_code
import data
from localizadores import message_for_driver


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

    def test_complete_taxi_request(self):
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
        print(f"Información del conductor: {driver_info}")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
