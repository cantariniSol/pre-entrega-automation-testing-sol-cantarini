from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage

BIKE_LIGHT = "sauce-labs-bike-light"
BACKPACK = "sauce-labs-backpack"
FLEECE = "sauce-labs-fleece-jacket"
BOLT = "sauce-labs-bolt-t-shirt"


def test_carrito(driver_logueado):
    """Agrega, quita y vuelve a agregar productos validando contador y carrito."""
    inventario = InventoryPage(driver_logueado)
    carrito = CartPage(driver_logueado)
    checkout = CheckoutPage(driver_logueado)

    # 1. Agregar Bike Light y verificar el carrito
    inventario.agregar_producto(BIKE_LIGHT)
    assert inventario.esperar_cantidad(1)
    inventario.abrir_carrito()
    assert carrito.nombres_productos() == ["Sauce Labs Bike Light"]

    # 2. Quitarla: el carrito queda vacío
    carrito.quitar_producto(BIKE_LIGHT)
    assert inventario.carrito_vacio()
    assert carrito.nombres_productos() == []
    carrito.seguir_comprando()

    # 3. Agregar Backpack y Bike Light
    inventario.agregar_producto(BACKPACK)
    inventario.agregar_producto(BIKE_LIGHT)
    assert inventario.esperar_cantidad(2)
    inventario.abrir_carrito()
    assert sorted(carrito.nombres_productos()) == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    # 4. Checkout, cancelar y volver al catálogo
    carrito.ir_a_checkout()
    checkout.cancelar()
    carrito.seguir_comprando()

    # 5. Agregar Fleece Jacket y Bolt T-Shirt: 4 en total
    inventario.agregar_producto(FLEECE)
    inventario.agregar_producto(BOLT)
    assert inventario.esperar_cantidad(4)

    # 6. Verificar los 4 productos en el carrito
    inventario.abrir_carrito()
    assert len(carrito.nombres_productos()) == 4, "El carrito debería tener 4 productos"