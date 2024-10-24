from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

# Registro del usuario
class SignUP(BasePage):
    buttonsign = (By.XPATH, "//a[@href='/auth/sign-up']")
    fullname_form = (By.XPATH, "//input[@id='full-name']")
    email_form = (By.XPATH, "//input[@id='email']")
    password_form = (By.XPATH, "//input[@id='password']")
    repeat_form = (By.XPATH, "//input[@id='confirm-password']")
    signup_form = (By.XPATH, "//button[contains(.,'Sign up')]")

    def select_button(self):
        self.wait_for_element(self.buttonsign).click()

    def set_fullname(self, name):
        self.wait_for_element(self.fullname_form).send_keys(name)

    def set_email(self, email):
        self.wait_for_element(self.email_form).send_keys(email)

    def set_password(self, password):
        self.wait_for_element(self.password_form).send_keys(password)

    def set_repeat(self, repeat):
        self.wait_for_element(self.repeat_form).send_keys(repeat)

    def submit_signup(self):
        self.wait_for_element(self.signup_form).click()


#Inicio se sesion
class SignIN(BasePage):
    emaillogin = (By.XPATH, "//input[@id='email']")
    passwordlogin = (By.XPATH, "//input[@id='password']")
    buttonlogin = (By.XPATH, "//button[contains(.,'Sign in')]")

    def set_email(self, email):
        self.wait_for_element(self.emaillogin).send_keys(email)

    def set_password(self, password):
        self.wait_for_element(self.passwordlogin).send_keys(password)

    def submit_login(self):
        self.wait_for_element(self.buttonlogin).click()


# Cerrar sesion
class Logout(BasePage):
    perfil = (By.XPATH, "//img[@src='/assets/rengoku.webp']")
    buttoncloseLog = (By.XPATH, "//a[contains(.,'Logout')]")

    def click_perfil(self):
        self.wait_for_element(self.perfil).click()

    def click_logout(self):
        self.wait_for_element(self.buttoncloseLog).click()