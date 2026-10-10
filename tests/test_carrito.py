from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers.clicConEspera import clic_con_espera

BADGE = (By.CLASS_NAME, "shopping_cart_badge")
CARRITO = (By.CLASS_NAME, "shopping_cart_link")


def verificar_badge(wait, esperado):
    """Verifica que el contador del carrito muestre la cantidad esperada."""
    badge = wait.until(EC.visibility_of_element_located(BADGE))
    assert badge.text == str(esperado), f"Se esperaban {esperado} ítems, hay {badge.text}"


def nombres_en_carrito(wait):
    """Devuelve los nombres de los productos listados en la página del carrito."""
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    return [i.find_element(By.CLASS_NAME, "inventory_item_name").text for i in items]


def test_carrito(driver_logueado, wait):
    """Agrega, quita y vuelve a agregar productos validando el contador y el carrito."""
    driver = driver_logueado
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"

    # 1. Agregar Bike Light y abrir el carrito
    clic_con_espera(driver, (By.ID, "add-to-cart-sauce-labs-bike-light"))
    verificar_badge(wait, 1)
    clic_con_espera(driver, CARRITO)
    wait.until(EC.url_contains("/cart.html"))
    assert nombres_en_carrito(wait) == ["Sauce Labs Bike Light"]

    # 2. Quitarla y volver a comprar: el carrito queda vacío
    clic_con_espera(driver, (By.ID, "remove-sauce-labs-bike-light"))
    wait.until(EC.invisibility_of_element_located(BADGE))
    assert driver.find_elements(By.CLASS_NAME, "cart_item") == [], "El carrito debería estar vacío"
    clic_con_espera(driver, (By.ID, "continue-shopping"))
    wait.until(EC.url_contains("/inventory.html"))

    # 3. Agregar Backpack y Bike Light, y abrir el carrito con 2 ítems
    clic_con_espera(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
    clic_con_espera(driver, (By.ID, "add-to-cart-sauce-labs-bike-light"))
    verificar_badge(wait, 2)
    clic_con_espera(driver, CARRITO)
    wait.until(EC.url_contains("/cart.html"))
    assert sorted(nombres_en_carrito(wait)) == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    # 4. Iniciar el checkout, cancelar y volver al catálogo
    clic_con_espera(driver, (By.ID, "checkout"))
    wait.until(EC.url_contains("/checkout-step-one.html"))
    clic_con_espera(driver, (By.ID, "cancel"))
    wait.until(EC.url_contains("/cart.html"))
    clic_con_espera(driver, (By.ID, "continue-shopping"))
    wait.until(EC.url_contains("/inventory.html"))

    # 5. Agregar Fleece Jacket y Bolt T-Shirt: el contador debe marcar 4
    clic_con_espera(driver, (By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
    clic_con_espera(driver, (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
    verificar_badge(wait, 4)

    # 6. Abrir el carrito y verificar los 4 productos
    clic_con_espera(driver, BADGE)
    wait.until(EC.url_contains("/cart.html"))
    assert len(nombres_en_carrito(wait)) == 4, "El carrito debería tener 4 productos"