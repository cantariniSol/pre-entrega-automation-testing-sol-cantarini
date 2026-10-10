from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.clicConEspera import clic_con_espera

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
    clic_con_espera(driver, (By.ID, "login-button"))

    # 3. Espera explícita: esperar a que cargue el inventario
    wait.until(EC.url_contains("/inventory.html"))

    # 4. Validaciones
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"

    titulo_pagina = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text
    assert titulo_pagina == "Products", f"Encabezado inesperado: {titulo_pagina}"


def test_login_password_incorrecta(driver_logueado, wait):
    """Caso negativo: tras cerrar sesión, una contraseña incorrecta muestra error y no ingresa."""
    driver = driver_logueado

    # 1. Ir al carrito y cerrar sesión desde el menú
    driver.get(URL + "cart.html")
    clic_con_espera(driver, (By.ID, "react-burger-menu-btn"))
    clic_con_espera(driver, (By.ID, "logout_sidebar_link"))
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert driver.current_url == URL, f"No se volvió al login: {driver.current_url}"

    # 2. Intentar ingresar con contraseña incorrecta
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USUARIO)
    driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
    clic_con_espera(driver, (By.ID, "login-button"))

    # 3. Validar el mensaje de error y que no se accedió al inventario
    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))).text
    assert error == "Epic sadface: Username and password do not match any user in this service", (
        f"Mensaje de error inesperado: {error}"
    )
    assert "/inventory.html" not in driver.current_url, "No debería haber ingresado al inventario"

    # 4. Corregir la contraseña y comprobar que ahora sí ingresa
    campo_password = driver.find_element(By.ID, "password")
    campo_password.clear()
    campo_password.send_keys(PASSWORD)
    clic_con_espera(driver, (By.ID, "login-button"))
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se ingresó con la contraseña correcta"