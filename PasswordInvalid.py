from selenium import webdriver
import time
import Data
from Page import SignUP, SignIN, Logout


class TestUser:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_user_registration_invalid_email(self):
        #Prueba para validar que la contraseña cumple con los requisitos de longitud y caracteres
        self.driver.get(Data.signup_url)
        signup_page = SignUP(self.driver)

        signup_page.select_button()
        signup_page.set_fullname(Data.name)
        signup_page.set_email(Data.email)
        signup_page.set_password("word")   # Contraseña inválido
        signup_page.set_repeat(Data.password)
        signup_page.submit_signup()

        assert "El correo debe cumplir con el estándar de una dirección de correo electrónico" in self.driver.page_source, "Error: Validación de email no valido."

    def test_user_login(self):
        #Prueba para iniciar sesión con una contraseña no valida
        self.driver.get(Data.signin_url)
        login_page = SignIN(self.driver)

        login_page.set_email(Data.email)
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