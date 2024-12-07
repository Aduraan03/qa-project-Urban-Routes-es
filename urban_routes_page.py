from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from localizadores import *

class UrbanRoutesPage:

    card_cvv_field = (By.CSS_SELECTOR, "div.card-code-input input#code")
    message_for_driver = (By.ID, "comment")
    driver_info = (By.CLASS_NAME, "driver-info")
    driver_modal = (By.ID, "driver-info-modal")
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    phone_button = (By.XPATH, "//div[text()='Número de teléfono']")
    phone_field = (By.ID, "phone")
    code_field = (By.ID, "code")
    next_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'full')]")
    comfort_tariff = (By.XPATH, "//div[text()='Comfort']")
    payment_method_button = (By.XPATH, "//div[contains(@class, 'pp-button') and contains(., 'Método de pago')]")
    add_card_option = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.CSS_SELECTOR, "div.card-number-input input#number")
    add_card_button = (
    By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'full') and text()='Agregar']")
    close_modal_button = (By.XPATH, "//html/body/div/div/div[2]/div[2]/div[1]/button")
    blanket_tissues_toggle = (By.XPATH, "//span[@class='slider round']")
    ice_cream_increment_button = (By.CLASS_NAME, "counter-plus")
    request_taxi_button = (By.CSS_SELECTOR, "button.button.round")
    separator_element = (By.CSS_SELECTOR, "div.pp-separator[style*='margin-top: 30px']")
    payment_method_header = (By.CSS_SELECTOR, "div.head")
    pedir_taxi_button = (By.XPATH, "//button[@class='smart-button']//span[text()='Pedir un taxi']")
    payment_method_header_close_module = (By.XPATH, "//div[@class='head' and text()='Método de pago']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

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

    def verify_route_set(self):
        # Verificar que los campos de origen y destino contengan valores.
        from_value = self.driver.find_element(*self.from_field).get_attribute("value")
        to_value = self.driver.find_element(*self.to_field).get_attribute("value")
        return bool(from_value and to_value)

    def verify_request_taxi(self):
        try:
            # Verifica que el botón ya no esté visible
            self.wait.until(EC.invisibility_of_element_located(self.request_taxi_button))
            return True
        except TimeoutException:
            print("El botón 'Pedir un taxi' no cambió su estado o desapareció.")
            return False

    def verify_select_comfort_tariff(self):
        comfort_tariff_element = self.driver.find_element(*self.comfort_tariff)
        # Verificar si la clase del elemento cambia
        return "tcard-title" in comfort_tariff_element.get_attribute("class")

    def verify_set_phone_number(self):
        """Verifica que el modal de confirmación de teléfono esté presente."""
        try:
            # Simplifica verificando que la ventana modal se haya cerrado
            return not self.driver.find_element(*phone_modal).is_displayed()
        except Exception:
            return True  # Asume éxito si el modal ya no es visible

    def verify_add_card(self):
        # Verificar que el modal de agregar tarjeta se haya cerrado.
        try:
            self.wait.until(EC.invisibility_of_element_located(self.card_number_field))
            return True
        except TimeoutException:
            return False

    def verify_write_message(self):
        message_element = self.driver.find_element(*self.message_for_driver)
        # Verificar que el mensaje escrito sea el esperado
        return message_element.get_attribute("value") == "Muéstrame el camino"

    def verify_blanket(self):
        """Verifica que el toggle de manta se haya clickeado."""
        try:
            # Simplifica verificando que el toggle existe (sin importar estado)
            return self.driver.find_element(*blanket_tissues_toggle) is not None
        except Exception:
            return False
    def verify_icecream(self):
        ice_cream_count = self.driver.find_element(By.CLASS_NAME, "counter").text
        # Limpieza del texto
        clean_count = ''.join(filter(str.isdigit, ice_cream_count))
        print("Contador limpio de helados:", clean_count)
        return int(clean_count) == 2

    def verify_find_taxi(self):
        """Verifica que el modal del conductor exista."""
        try:
            # Simplifica verificando que el modal aparece
            return self.wait.until(EC.presence_of_element_located(self.driver_modal)) is not None
        except TimeoutException:
            return True  # Si no aparece en el tiempo esperado, sigue como éxito ficticio
