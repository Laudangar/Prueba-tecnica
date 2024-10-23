import Data
from selenium import webdriver
from Page import SignUP, SignIN, Logout
import time

class testUser:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.home = Data.signin_url
        cls.driver.get(cls.home)

    def test_selectbuttonsign(self):
        Page = SignUP(self.driver)
        Page.select_button()
        time.sleep(2)

    def test_set_form_correct(self):
        Page = SignUP(self.driver)
        name = Data.name
        email = Data.email
        password = Data.password
        repeat = Data.password
        Page.set_fullname(name)
        Page.set_email(email)
        Page.set_password(password)
        Page.set_repead(repeat)
        assert Page.get_fullname() == name
        assert Page.get_email() == email
        assert Page.get_password() == password
        assert Page.get_repeat() == repeat
        time.sleep(2)

    def test_fullname_minimum(self):
        Page = SignUP(self.driver)
        Page.set_fullname("Laura")
        Page.set_email("Laura@gmail.com")
        Page.set_password("Laura12$")
        Page.set_repeat("Laura12$")
        assert "Full name must contain at least 2 words" in self.driver.page_source, "Error: El nombre de usuario no está validando la longitud mínima de dos palabras."

    def test_login(self):
        Page = SignIN(self.driver)
        email = Data.email
        password = Data.password
        Page.set_emailSignIN(email)
        Page.set_passwordSignIN(password)
        Page.click_loginSignIN()
        time.sleep(2)

        # Verificar que el nombre del usuario se muestra después de iniciar sesión
        assert "Laura Garcia" in self.driver.page_source, "Error: No se ha iniciado sesión correctamente."

    def test_logout(self):
        Page = Logout(self.driver)
        Page.click_logout()
        time.sleep(2)
        # Verificar que el usuario ha cerrado sesión correctamente
        assert "Sign in" in self.driver.page_source, "Error: No se ha cerrado la sesión correctamente."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


