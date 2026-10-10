from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configs.config import TIMEOUT
from configs.logger import obtener_logger
from helpers.clicConEspera import clic_con_espera

logger = obtener_logger(__name__)


class BasePage:
    """Métodos comunes a todas las páginas."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def abrir(self, url):
        logger.info("Abrir URL: %s", url)
        self.driver.get(url)

    def clic(self, localizador):
        logger.info("Clic en %s", localizador)
        clic_con_espera(self.driver, localizador)

    def escribir(self, localizador, texto):
        logger.info("Escribir en %s", localizador)
        campo = self.wait.until(EC.visibility_of_element_located(localizador))
        campo.clear()
        campo.send_keys(texto)

    def texto(self, localizador):
        valor = self.wait.until(EC.visibility_of_element_located(localizador)).text
        logger.info("Texto de %s: %s", localizador, valor)
        return valor

    def esperar_url(self, fragmento):
        logger.info("Esperar URL que contenga: %s", fragmento)
        self.wait.until(EC.url_contains(fragmento))

    def existe(self, localizador):
        return len(self.driver.find_elements(*localizador)) > 0