from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITULO = (By.CLASS_NAME, "title")
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    NOMBRE = (By.CLASS_NAME, "inventory_item_name")
    PRECIO = (By.CLASS_NAME, "inventory_item_price")
    BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")

    def esta_en_inventario(self):
        self.esperar_url("/inventory.html")
        return self.texto(self.TITULO) == "Products"

    def listar_productos(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.PRODUCTOS))

    def datos_primer_producto(self):
        primero = self.listar_productos()[0]
        return (
            primero.find_element(*self.NOMBRE).text,
            primero.find_element(*self.PRECIO).text,
        )

    def agregar_producto(self, id_producto):
        # id_producto ejemplo: "sauce-labs-backpack"
        self.clic((By.ID, f"add-to-cart-{id_producto}"))

    def quitar_producto(self, id_producto):
        self.clic((By.ID, f"remove-{id_producto}"))

    def cantidad_en_carrito(self):
        if not self.existe(self.BADGE):
            return 0
        return int(self.texto(self.BADGE))

    def abrir_carrito(self):
        self.clic(self.CARRITO)
        self.esperar_url("/cart.html")

    def abrir_detalle(self, nombre_producto):
        self.clic((By.XPATH, f"//div[normalize-space()='{nombre_producto}']"))

    def esperar_cantidad(self, cantidad):
        """Espera a que el contador del carrito muestre la cantidad indicada."""
        return self.wait.until(
            EC.text_to_be_present_in_element(self.BADGE, str(cantidad))
        )

    def carrito_vacio(self):
        """Espera a que el contador del carrito desaparezca."""
        return self.wait.until(EC.invisibility_of_element_located(self.BADGE))
        
        
