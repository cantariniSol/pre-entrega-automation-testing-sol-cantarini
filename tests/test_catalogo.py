from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers.clicConEspera import clic_con_espera

PRODUCTO_REMERA = "Test.allTheThings() T-Shirt (Red)"
PRODUCTO_MOCHILA = "Sauce Labs Backpack"


def nombre_en_detalle(wait):
    """Devuelve el nombre del producto mostrado en la página de detalle."""
    return wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name"))
    ).text


def test_catalogo(driver_logueado, wait):
    """Valida el catálogo y recorre detalle de productos, agregar y quitar del carrito."""
    # 1. Validaciones del catálogo
    assert driver_logueado.title == "Swag Labs", f"Título inesperado: {driver_logueado.title}"

    productos = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(productos) > 0, "No hay productos en el catálogo"

    primero = productos[0]
    nombre = primero.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primero.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert nombre != "", "El primer producto no tiene nombre"
    assert precio.startswith("$"), f"Precio con formato inesperado: {precio}"
    print(f"Primer producto: {nombre} - {precio}")

    # 2. Abrir el detalle de la remera roja y volver al catálogo
    clic_con_espera(driver_logueado, (By.XPATH, f"//div[normalize-space()='{PRODUCTO_REMERA}']"))
    wait.until(EC.url_contains("/inventory-item.html"))
    assert nombre_en_detalle(wait) == PRODUCTO_REMERA, "El detalle no corresponde a la remera roja"

    clic_con_espera(driver_logueado, (By.ID, "back-to-products"))
    wait.until(EC.url_contains("/inventory.html"))

    # 3. Agregar la mochila al carrito desde el catálogo
    clic_con_espera(driver_logueado, (By.ID, "add-to-cart-sauce-labs-backpack"))
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1", f"Se esperaba 1 ítem en el carrito, hay {badge.text}"

    # 4. Abrir el detalle de la mochila y quitarla del carrito
    clic_con_espera(driver_logueado, (By.XPATH, f"//div[normalize-space()='{PRODUCTO_MOCHILA}']"))
    wait.until(EC.url_contains("/inventory-item.html"))
    assert nombre_en_detalle(wait) == PRODUCTO_MOCHILA, "El detalle no corresponde a la mochila"

    clic_con_espera(driver_logueado, (By.ID, "remove"))
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    # 5. Volver al catálogo
    clic_con_espera(driver_logueado, (By.ID, "back-to-products"))
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver_logueado.current_url, "No se volvió al catálogo"
