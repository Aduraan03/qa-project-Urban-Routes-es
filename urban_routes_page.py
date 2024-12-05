from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from localizadores import *  # Importa los localizadores desde localizadores.py

class UrbanRoutesPage:
    card_cvv_field = (By.CSS_SELECTOR, "div.card-code-input input#code")
    message_for_driver = (By.ID, "comment")
    driver_info = (By.CLASS_NAME, "driver-info")
    driver_modal = (By.ID, "driver-info-modal")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def send_enter(self):
        """Simula la tecla Enter en el elemento activo."""
        active_element = self.driver.switch_to.active_element
        active_element.send_keys(Keys.ENTER)

    def set_route(self, from_address, to_address):
        self.wait.until(EC.presence_of_element_located(from_field))
        self.driver.find_element(*from_field).send_keys(from_address)

        self.wait.until(EC.presence_of_element_located(to_field))
        self.driver.find_element(*to_field).send_keys(to_address)

    def request_taxi(self):
        """Solicita un taxi (con manejo de excepciones)."""
        try:
            self.wait.until(EC.element_to_be_clickable(request_taxi_button)).click()
        except TimeoutException:
            print("El botón 'Pedir un taxi' no se hizo clickeable a tiempo.")
            self.wait.until(EC.element_to_be_clickable(request_taxi_button)).click()

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(comfort_tariff)).click()

    def open_phone_modal(self):
        self.wait.until(EC.element_to_be_clickable(phone_button)).click()

    def fill_phone_number(self, phone_number):
        phone_input = self.wait.until(EC.visibility_of_element_located(phone_field))
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def click_next_button(self):
        next_btn = self.wait.until(EC.element_to_be_clickable(next_button))
        next_btn.click()
        self.driver.implicitly_wait(2)

    def enter_confirmation_code(self, confirmation_code):
        code_input = self.wait.until(EC.visibility_of_element_located(code_field))
        code_input.clear()
        code_input.send_keys(confirmation_code)
        code_input.send_keys(Keys.TAB)
        self.send_enter()

    def click_payment_method_button(self):
        self.wait.until(EC.element_to_be_clickable(payment_method_button)).click()

    def click_add_card_option(self):
        self.wait.until(EC.element_to_be_clickable(add_card_option)).click()

    def fill_card_number(self, card_number):
        """Llenar el campo de número de tarjeta."""
        card_input_field = self.wait.until(EC.visibility_of_element_located(card_number_field))
        card_input_field.clear()
        card_input_field.send_keys(card_number)

    def fill_cvv(self, card_code):
        """Llenar el campo del código CVV."""
        card_cvv_input = self.wait.until(EC.visibility_of_element_located(self.card_cvv_field))
        card_cvv_input.clear()
        card_cvv_input.send_keys(card_code)
        card_cvv_input.send_keys(Keys.ENTER)  # Simula Enter después de llenar el CVV

    def click_add_card_button(self):
        separator = self.wait.until(EC.element_to_be_clickable(separator_element))
        separator.click()
        self.wait.until(EC.element_to_be_clickable(add_card_button)).click()

    def close_modal(self):
        self.wait.until(EC.element_to_be_clickable(close_modal_button)).click()

    def write_message_for_driver(self, message):
        """Escribir mensaje para el conductor."""
        message_field = self.wait.until(
            EC.visibility_of_element_located(self.message_for_driver))  # Espera a que sea visible
        message_field.clear()  # Limpiar cualquier valor previo
        message_field.send_keys(message)  # Escribir el mensaje

    def toggle_blanket_tissues(self):
        self.wait.until(EC.element_to_be_clickable(blanket_tissues_toggle)).click()

    def increment_ice_cream_count(self, count):
        button = self.driver.find_element(*ice_cream_increment_button)
        for _ in range(count):
            button.click()

    def click_pedir_taxi(self):
        self.wait.until(EC.element_to_be_clickable(pedir_taxi_button)).click()

    def wait_for_driver_info(self):
        try:
            # Esperar explícitamente a que el modal sea visible
            self.wait.until(EC.visibility_of_element_located(self.driver_modal))
            return self.driver.find_element(*self.driver_info).text
        except TimeoutException:
            print("El modal del conductor no se ha cargado en el tiempo esperado.")
            return None
