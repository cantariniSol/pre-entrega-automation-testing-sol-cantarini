from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    ITEMS = (By.CLASS_NAME, "cart_item")
    NOMBRE = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT = (By.ID, "checkout")
    CONTINUAR = (By.ID, "continue-shopping")
    QUITAR_TEMPLATE = "remove-{}"

    def nombres_productos(self):
        self.esperar_url("/cart.html")
        items = self.driver.find_elements(*self.ITEMS)
        return [i.find_element(*self.NOMBRE).text for i in items]

    def quitar_producto(self, id_producto):
        self.clic((By.ID, self.QUITAR_TEMPLATE.format(id_producto)))

    def ir_a_checkout(self):
        self.clic(self.CHECKOUT)
        self.esperar_url("/checkout-step-one.html")

    def seguir_comprando(self):
        self.clic(self.CONTINUAR)
        self.esperar_url("/inventory.html")