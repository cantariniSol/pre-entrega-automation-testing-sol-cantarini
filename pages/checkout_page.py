from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    CODIGO_POSTAL = (By.ID, "postal-code")
    CONTINUAR = (By.ID, "continue")
    CANCELAR = (By.ID, "cancel")
    FINALIZAR = (By.ID, "finish")
    PRODUCTO_RESUMEN = (By.CLASS_NAME, "inventory_item_name")
    MENSAJE_FINAL = (By.CLASS_NAME, "complete-header")

    def completar_datos(self, nombre, apellido, codigo_postal):
        self.escribir(self.NOMBRE, nombre)
        self.escribir(self.APELLIDO, apellido)
        self.escribir(self.CODIGO_POSTAL, codigo_postal)
        self.clic(self.CONTINUAR)
        self.esperar_url("/checkout-step-two.html")

    def cancelar(self):
        self.clic(self.CANCELAR)
        self.esperar_url("/cart.html")

    def producto_en_resumen(self):
        return self.texto(self.PRODUCTO_RESUMEN)

    def finalizar(self):
        self.clic(self.FINALIZAR)
        self.esperar_url("/checkout-complete.html")

    def mensaje_final(self):
        return self.texto(self.MENSAJE_FINAL)