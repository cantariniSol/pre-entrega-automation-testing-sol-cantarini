from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage

PRODUCTO = "Sauce Labs Bike Light"


def test_compra_completa(driver_logueado):
    """Flujo completo: producto, carrito, checkout y finalizar compra."""
    inventario = InventoryPage(driver_logueado)
    producto = ProductPage(driver_logueado)
    carrito = CartPage(driver_logueado)
    checkout = CheckoutPage(driver_logueado)

    inventario.abrir_detalle(PRODUCTO)
    assert producto.nombre() == PRODUCTO
    producto.agregar()
    assert inventario.esperar_cantidad(1)

    inventario.abrir_carrito()
    assert carrito.nombres_productos() == [PRODUCTO]

    carrito.ir_a_checkout()
    checkout.completar_datos("María Sol", "Cantarini", "5152")
    assert checkout.producto_en_resumen() == PRODUCTO

    checkout.finalizar()
    assert checkout.mensaje_final() == "Thank you for your order!"