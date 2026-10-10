from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
PASSWORD = "secret_sauce"


def test_login_exitoso(driver):
    """Login válido: redirige a /inventory.html y muestra 'Products'."""
    wait = WebDriverWait(driver, 10)

    # 1. Navegar a la página de login
    driver.get(URL)

    # 2. Ingresar credenciales
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USUARIO)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # 3. Espera explícita: esperar a que cargue el inventario
    wait.until(EC.url_contains("/inventory.html"))

    # 4. Validaciones
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"

    titulo_pagina = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text
    assert titulo_pagina == "Products", f"Encabezado inesperado: {titulo_pagina}"