from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://test-qa.inlaze.com/register')

# Llenar el formulario
buttonsign = (By.XPATH, "//a[@href='/auth/sign-up']")
driver.find_element(By.XPATH, "//input[@id='full-name']").send_keys('Juan Pérez')
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('juanperez@test.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Password@123')
driver.find_element(By.XPATH, "//input[@id='confirm-password']").send_keys('Password@123')


# Enviar el formulario
driver.find_element = (By.XPATH, "//button[contains(.,'Sign up')]").click()

# Esperar para verificar el resultado
time.sleep(5)

# Verificar si el registro fue exitoso
assert "Registro exitoso" in driver.page_source, "Error: El registro no fue exitoso."

driver.get('https://test-qa.inlaze.com/register')

# Llenar el formulario con un nombre inválido
buttonsign = (By.XPATH, "//a[@href='/auth/sign-up']")
driver.find_element(By.XPATH, "//input[@id='full-name']").send_keys('Juan')
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('juanperez@test.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Password@123')
driver.find_element(By.XPATH, "//input[@id='confirm-password']").send_keys('Password@123')

# Enviar el formulario
driver.find_element = (By.XPATH, "//button[contains(.,'Sign up')]").click()

# Esperar para verificar el resultado
time.sleep(5)

# Verificar el mensaje de error
assert "El nombre debe tener al menos 2 palabras" in driver.page_source, "Error: La validación de nombre no funcionó."

driver.get('https://test-qa.inlaze.com/login')

# Llenar el formulario de login
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('juanperez@test.com')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Password@123')

# Enviar el formulario
driver.find_element(By.XPATH, "//button[contains(.,'Sign in')]").click()

# Esperar para verificar el resultado
time.sleep(5)

# Verificar que el nombre del usuario esté presente
assert "Juan Pérez" in driver.page_source, "Error: El login no fue exitoso."

driver.quit()
