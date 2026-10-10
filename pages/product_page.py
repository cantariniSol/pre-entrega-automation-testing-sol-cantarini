from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    NOMBRE = (By.CLASS_NAME, "inventory_details_name")
    VOLVER = (By.ID, "back-to-products")
    AGREGAR = (By.ID, "add-to-cart")
    QUITAR = (By.ID, "remove")

    def nombre(self):
        self.esperar_url("/inventory-item.html")
        return self.texto(self.NOMBRE)

    def agregar(self):
        self.clic(self.AGREGAR)

    def quitar(self):
        self.clic(self.QUITAR)

    def volver_a_productos(self):
        self.clic(self.VOLVER)
        self.esperar_url("/inventory.html")