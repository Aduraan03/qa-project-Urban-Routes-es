#Correr el pytest en test_urban_routes.py

"""import data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            print(logs)  # Depuración para verificar los logs
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(3)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    # Localizadores
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
    card_cvv_field = (By.CSS_SELECTOR, "div.card-code-input input#code")
    add_card_button = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'full') and text()='Agregar']")
    close_modal_button = (By.XPATH, "//html/body/div/div/div[2]/div[2]/div[1]/button")
    message_for_driver = (By.ID, "comment")
    blanket_tissues_toggle = (By.XPATH, "//span[@class='slider round']")
    ice_cream_increment_button = (By.CLASS_NAME, "counter-plus")
    request_taxi_button = (By.CSS_SELECTOR, "button.button.round")
    driver_modal = (By.ID, "driver-info-modal")
    driver_info = (By.CLASS_NAME, "driver-info")
    separator_element = (By.CSS_SELECTOR, "div.pp-separator[style*='margin-top: 30px']")
    payment_method_header = (By.CSS_SELECTOR, "div.head")
    pedir_taxi_button = (By.XPATH, "//button[@class='smart-button']//span[text()='Pedir un taxi']")
    payment_method_header_close_module = (By.XPATH, "//div[@class='head' and text()='Método de pago']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def send_enter(self):
        """Simula la tecla Enter en el elemento activo."""
        active_element = self.driver.switch_to.active_element
        active_element.send_keys(Keys.ENTER)

    def set_route(self, from_address, to_address):
        # Esperar a que los campos estén disponibles antes de interactuar
        self.wait.until(EC.presence_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

        self.wait.until(EC.presence_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def request_taxi(self):
        """Solicita un taxi (con manejo de excepciones)."""
        try:
            # Intentar hacer clic en el botón 'Pedir un taxi' para solicitar un taxi
            self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)).click()
        except TimeoutException:
            print("El botón 'Pedir un taxi' no se hizo clickeable a tiempo. Intentando buscarlo nuevamente.")
            # Intentamos buscar el botón nuevamente
            self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)).click()
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff)).click()

    def open_phone_modal(self):
        # Hacer clic en el botón "Número de teléfono" para abrir la ventana emergente
        self.wait.until(EC.element_to_be_clickable(self.phone_button)).click()

    def fill_phone_number(self, phone_number):
        # Esperar a que el campo del teléfono esté visible y luego llenarlo
        phone_input = self.wait.until(EC.visibility_of_element_located(self.phone_field))
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def click_next_button(self):
        # Hacer clic en el botón "Siguiente" y esperar 2 segundos
        next_btn = self.wait.until(EC.element_to_be_clickable(self.next_button))
        next_btn.click()
        self.driver.implicitly_wait(2)  # Espera de 2 segundos después de presionar el botón

    def enter_confirmation_code(self, confirmation_code):
        # Esperar a que el campo de código esté visible y luego ingresarlo
        code_input = self.wait.until(EC.visibility_of_element_located(self.code_field))
        code_input.clear()
        code_input.send_keys(confirmation_code)
        code_input.send_keys(Keys.TAB)
        self.send_enter()  # Simula Enter después de ingresar el código

    def click_payment_method_button(self):
        """Abre el modal 'Método de pago'."""
        self.wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()

    def click_add_card_option(self):
        self.wait.until(EC.element_to_be_clickable(self.add_card_option)).click()

    def fill_card_number(self, card_number):
        """Llenar el campo de número de tarjeta."""
        card_number_field = self.wait.until(EC.visibility_of_element_located(self.card_number_field))
        card_number_field.clear()
        card_number_field.send_keys(card_number)

    def fill_cvv(self, card_code):
        """Llenar el campo del código CVV."""
        card_cvv_field = self.wait.until(EC.visibility_of_element_located(self.card_cvv_field))
        card_cvv_field.clear()
        card_cvv_field.send_keys(card_code)
        card_cvv_field.send_keys(Keys.ENTER)  # Simular Enter después de llenar el CVV

    def click_add_card_button(self):
        # Hacer clic en el separador
        separator = self.wait.until(EC.element_to_be_clickable(self.separator_element))
        separator.click()
        """Hacer clic en el botón 'Agregar' después de llenar los datos de la tarjeta."""
        self.wait.until(EC.element_to_be_clickable(self.add_card_button)).click()

    def close_modal(self):
        """Cerrar el modal de agregar tarjeta o cualquier otro modal."""
        self.wait.until(EC.element_to_be_clickable(self.close_modal_button)).click()

    def toggle_blanket_tissues(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_tissues_toggle)).click()
    def increment_ice_cream_count(self, count):
        button = self.driver.find_element(*self.ice_cream_increment_button)
        for _ in range(count):
            button.click()

    def click_pedir_taxi(self):
        """Haz clic en el botón de 'Pedir un taxi'."""
        try:
            # Esperamos que el botón esté clickeable y lo presionamos
            self.wait.until(EC.element_to_be_clickable(self.pedir_taxi_button)).click()
            print("Botón de 'Pedir un taxi' clickeado correctamente.")
        except TimeoutException:
            print("El botón de 'Pedir un taxi' no se hizo clickeable a tiempo.")

    def wait_for_driver_info(self):
        try:
            # Esperar explícitamente a que el modal sea visible
            self.wait.until(EC.visibility_of_element_located(self.driver_modal))
            return self.driver.find_element(*self.driver_info).text
        except TimeoutException:
            print("El modal del conductor no se ha cargado en el tiempo esperado.")
            return None

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.service import Service  # Importar el servicio

        # Crear opciones para el navegador
        options = Options()
        options.add_argument("--start-maximized")  # Maximizar el navegador al iniciar.

        # Configurar registros de rendimiento directamente en las opciones
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Configurar el servicio de ChromeDriver
        service = Service()  # Puedes especificar aquí la ruta a ChromeDriver si no está en PATH.

        # Inicializar el controlador con opciones
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_complete_taxi_request(self):
        print("Iniciando prueba")

        # Configurar las direcciones
        self.page.set_route(data.address_from, data.address_to)

        # Pedir un taxi (esto abre el modal de tarifas)
        self.page.request_taxi()

        # Seleccionar la tarifa Comfort
        self.page.select_comfort_tariff()

        # Abrir el modal de teléfono y llenar el número
        self.page.open_phone_modal()  # Abre la ventana emergente del número de teléfono
        self.page.fill_phone_number(data.phone_number)

        # Presionar el botón "Siguiente en telefono"
        self.page.click_next_button()

        # Confirmar el código de teléfono
        confirmation_code = retrieve_phone_code(self.driver)  # Recupera el código
        print(f"Código de confirmación: {confirmation_code}")

        # Llenar el código de confirmación
        self.page.enter_confirmation_code(confirmation_code)

        #  Agregar tarjeta
        self.page.click_payment_method_button()
        self.page.click_add_card_option()
        self.page.fill_card_number(data.card_number)
        self.page.fill_cvv(data.card_code)
        self.page.click_add_card_button()
        self.page.close_modal()

        #  Escribir mensaje para el conductor
        self.driver.find_element(*self.page.message_for_driver).send_keys(data.message_for_driver)
        # Pedir manta y pañuelos
        self.page.toggle_blanket_tissues()

        # Pedir 2 helados
        self.page.increment_ice_cream_count(2)

        # Hacer clic en el botón de 'Pedir taxi'
        self.page.click_pedir_taxi()

        # Verificar la información del conductor
        driver_info = self.page.wait_for_driver_info()
        assert driver_info != "", "La información del conductor no está disponible."
        print(f"Información del conductor: {driver_info}")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()"""
