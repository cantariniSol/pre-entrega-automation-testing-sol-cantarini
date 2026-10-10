from configs.config import PASSWORD, URL, USUARIO
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

MENSAJE_ERROR = "Epic sadface: Username and password do not match any user in this service"


def test_login_exitoso(driver):
    """Login válido: llega a /inventory.html, muestra 'Products' y título 'Swag Labs'."""
    login = LoginPage(driver)
    login.abrir_login()
    login.ingresar(USUARIO, PASSWORD)

    inventario = InventoryPage(driver)
    assert inventario.esta_en_inventario(), "No se llegó a Products en /inventory.html"
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"


def test_login_password_incorrecta(driver_logueado):
    """Caso negativo: contraseña incorrecta muestra error y no ingresa al inventario."""
    login = LoginPage(driver_logueado)
    login.abrir(URL + "cart.html")
    login.cerrar_sesion()

    login.ingresar(USUARIO, "clave_incorrecta")
    assert login.obtener_error() == MENSAJE_ERROR
    assert "/inventory.html" not in driver_logueado.current_url

    # Corregir la contraseña: ahora sí ingresa
    login.ingresar(USUARIO, PASSWORD)
    assert InventoryPage(driver_logueado).esta_en_inventario()