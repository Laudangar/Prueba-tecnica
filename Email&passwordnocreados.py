from selenium import webdriver
import time
import Data
from Pages import SignUP, SignIN, Logout


class TestUser:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_user_login(self):
        #Prueba para iniciar sesión con una contraseña no valida
        self.driver.get(Data.signin_url)
        login_page = SignIN(self.driver)

        login_page.set_email("l.com")
        login_page.set_password("word")
        login_page.submit_login()

        assert Data.name in self.driver.page_source, "Error: Inicio de sesión fallido."
        time.sleep(2)

    def test_logout(self):
        #Prueba para cerrar sesión correctamente
        logout_page = Logout(self.driver)
        logout_page.click_perfil()
        logout_page.click_logout()

        assert "Sign in" in self.driver.page_source, "Error: No se cerró la sesión correctamente."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()