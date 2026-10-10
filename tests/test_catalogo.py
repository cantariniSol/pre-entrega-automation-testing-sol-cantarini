from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage

REMERA = "Test.allTheThings() T-Shirt (Red)"
MOCHILA = "Sauce Labs Backpack"
ID_MOCHILA = "sauce-labs-backpack"


def test_catalogo(driver_logueado):
    """Valida el catálogo y recorre detalle, agregar y quitar productos."""
    inventario = InventoryPage(driver_logueado)
    producto = ProductPage(driver_logueado)

    # Catálogo
    assert driver_logueado.title == "Swag Labs"
    assert inventario.esta_en_inventario()
    assert len(inventario.listar_productos()) > 0, "No hay productos en el catálogo"

    nombre, precio = inventario.datos_primer_producto()
    assert nombre != "", "El primer producto no tiene nombre"
    assert precio.startswith("$"), f"Precio con formato inesperado: {precio}"
    print(f"Primer producto: {nombre} - {precio}")

    # Detalle de la remera y volver
    inventario.abrir_detalle(REMERA)
    assert producto.nombre() == REMERA
    producto.volver_a_productos()

    # Agregar la mochila desde el catálogo
    inventario.agregar_producto(ID_MOCHILA)
    assert inventario.esperar_cantidad(1)

    # Detalle de la mochila y quitarla
    inventario.abrir_detalle(MOCHILA)
    assert producto.nombre() == MOCHILA
    producto.quitar()
    assert inventario.carrito_vacio()

    producto.volver_a_productos()
    assert inventario.esta_en_inventario()