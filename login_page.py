from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def login(self, username, password):
        driver = self.driver

        login_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        login_input.send_keys(username)
        print('Логин введен')

        password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_input.send_keys(password)
        print("Пароль введен")

        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        login_button.click()
        print("Кнопка логина нажата")