from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configs.config import TIMEOUT
from helpers.clicConEspera import clic_con_espera


class BasePage:
    """Métodos comunes a todas las páginas."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def abrir(self, url):
        self.driver.get(url)

    def clic(self, localizador):
        clic_con_espera(self.driver, localizador)

    def escribir(self, localizador, texto):
        campo = self.wait.until(EC.visibility_of_element_located(localizador))
        campo.clear()
        campo.send_keys(texto)

    def texto(self, localizador):
        return self.wait.until(EC.visibility_of_element_located(localizador)).text

    def esperar_url(self, fragmento):
        self.wait.until(EC.url_contains(fragmento))

    def existe(self, localizador):
        return len(self.driver.find_elements(*localizador)) > 0