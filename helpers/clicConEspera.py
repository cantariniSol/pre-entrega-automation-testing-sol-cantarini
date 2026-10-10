import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PAUSA_VISUAL = 2  # segundos; poné 0 para correr rápido


def clic_con_espera(driver, localizador, pausa=PAUSA_VISUAL):
    """Espera a que el botón sea clickeable, hace una pausa visible y hace clic."""
    elemento = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(localizador))
    time.sleep(pausa)
    elemento.click()