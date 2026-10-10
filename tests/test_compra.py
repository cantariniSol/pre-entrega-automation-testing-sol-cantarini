from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers.clicConEspera import clic_con_espera


def test_compra_completa(driver_logueado, wait):
    """Flujo completo: elegir producto, carrito, checkout y finalizar compra."""
    # 1. Abrir el detalle de "Sauce Labs Bike Light"
    clic_con_espera(
        driver_logueado, (By.XPATH, "//div[normalize-space()='Sauce Labs Bike Light']")
    )

    # 2. Agregar al carrito
    clic_con_espera(driver_logueado, (By.ID, "add-to-cart"))

    # 3. Verificar el contador y abrir el carrito
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1", f"Se esperaba 1 ítem en el carrito, hay {badge.text}"
    clic_con_espera(driver_logueado, (By.CLASS_NAME, "shopping_cart_badge"))
    wait.until(EC.url_contains("/cart.html"))

    # 4. Checkout
    clic_con_espera(driver_logueado, (By.ID, "checkout"))
    wait.until(EC.url_contains("/checkout-step-one.html"))

    # 5. Completar datos personales
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("María Sol")
    driver_logueado.find_element(By.ID, "last-name").send_keys("Cantarini")
    driver_logueado.find_element(By.ID, "postal-code").send_keys("5152")
    clic_con_espera(driver_logueado, (By.ID, "continue"))

    # 6. Resumen: validar producto antes de finalizar
    wait.until(EC.url_contains("/checkout-step-two.html"))
    nombre = driver_logueado.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre == "Sauce Labs Bike Light", f"Producto inesperado en el resumen: {nombre}"

    # 7. Finalizar compra
    clic_con_espera(driver_logueado, (By.ID, "finish"))

    # 8. Validar compra exitosa
    wait.until(EC.url_contains("/checkout-complete.html"))
    mensaje = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
    assert mensaje == "Thank you for your order!", f"Mensaje inesperado: {mensaje}"