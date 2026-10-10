from selenium.webdriver.common.by import By

from configs.config import URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    USUARIO = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")
    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

    def abrir_login(self):
        self.abrir(URL)

    def ingresar(self, usuario, password):
        self.escribir(self.USUARIO, usuario)
        self.escribir(self.PASSWORD, password)
        self.clic(self.BOTON_LOGIN)

    def obtener_error(self):
        return self.texto(self.ERROR)

    def cerrar_sesion(self):
        self.clic(self.MENU)
        self.clic(self.LOGOUT)
