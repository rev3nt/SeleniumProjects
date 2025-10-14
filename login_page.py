from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def login(self, username, password):
        # Получаем драйвер из конструктора класса
        driver = self.driver

        # Находим локатор поля логина и вводим username
        login_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        login_input.send_keys(username)
        print('Логин введен')

        # Находим локатор поля пароля и вводим password
        password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_input.send_keys(password)
        print("Пароль введен")

        # Нажимаем на кнопку логина
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        login_button.click()
        print("Кнопка логина нажата")