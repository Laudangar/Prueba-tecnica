from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Llenar el formulario de creación de cuenta

class SignUP:
    buttonsign = (By.XPATH, "//a[@href='/auth/sign-up']")
    fullname_form = (By.XPATH, "//input[@id='full-name']")
    email_form = (By.XPATH, "//input[@id='email']")
    password_form = (By.XPATH, "//input[@id='password']")
    repeat_form = (By.XPATH, "//input[@id='confirm-password']")
    signup_form = (By.XPATH, "//button[contains(.,'Sign up')]")


    def __init__(self, driver):
        self.driver = driver


    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def select_button(self):
        self.driver.find_element(*self.buttonsign).click()

    def set_fullname(self,name):
        self.driver.find_element(*self.fullname_form).send_keys(name)

    def set_email(self,email):
        self.driver.find_element(*self.email_form).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(*self.password_form).send_keys(password)

    def set_repead(self,repead):
        self.driver.find_element(*self.repeat_form).send_keys(repead)

    def get_signup(self):
        self.driver.find_element(*self.signup_form).click()

    def get_fullname(self):
        return self.driver.find_element(*self.fullname_form).get_property('value')

    def get_email(self):
        return self.driver.find_element(*self.email_form).get_property('value')

    def get_password(self):
        return self.driver.find_element(*self.password_form).get_property('value')

    def get_repeat(self):
        return self.driver.find_element(*self.repeat_form).get_property('value')


    #Inicio de sesion

class SignIN:
    emaillogin = (By.XPATH, "//input[@id='email']")
    passwordlogin = (By.XPATH, "//input[@id='password']")
    buttonlogin = (By.XPATH, "//button[contains(.,'Sign in')]")

    def __init__(self, driver):
        self.driver = driver

    def set_emailSignIN(self, email):
        self.driver.find_element(*self.emaillogin).send_keys(email)

    def set_passwordSignIN(self, password):
        self.driver.find_element(*self.passwordlogin).send_keys(password)

    def click_loginSignIN(self):
        self.driver.find_element(*self.buttonlogin).click()

    #Cerrado de sesion

class Logout:
    perfil = (By.XPATH, "//img[@src='/assets/rengoku.webp']")
    buttoncloseLog = (By.XPATH, "//a[contains(.,'Logout')]")

    def __init__(self, driver):
        self.driver = driver

    def click_perfil(self):
        self.driver.find_element(*self.perfil).click()

    def click_logout(self):
        self.driver.find_element(*self.buttoncloseLog).click()

