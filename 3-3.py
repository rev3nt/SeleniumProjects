import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


class Test:
    def __init__(self, base_url):
        # Сохраняем базовый url, с котором будет проводиться тестирование
        self.base_url = base_url

        # Инициализируем необходимый драйвер
        self.__init_chrome_driver()

    def __init_chrome_driver(self):
        # Настройки перед запуском браузера
        options = webdriver.ChromeOptions()
        # Опция, позволяющая сохранять браузер открытым после выполнения скрипта
        options.add_experimental_option('detach', True)
        # Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
        options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

        # Создаем драйвер для управления Chrome
        self.driver = webdriver.Chrome(options=options)

    def test_login_and_adding_in_cart(self, username, password):
        # Открытие ссылки в браузере
        self.driver.get(self.base_url)
        # Развертывание окна браузера на полный экран
        self.driver.maximize_window()

        # Создаем экземпляр класса для логина пользователя
        login_page = LoginPage(self.driver)
        # Проводим процедуру логина
        login_page.login(username, password)

        # Добавляем товар в корзину
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        print("Товар добавлен в корзину")

        # Переходим на страницу корзины
        go_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        go_cart_button.click()
        print("Переход в корзину")

        # Находим текст, с которым будем сверяться, успешен ли переход на страницу корзины или нет
        success_title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='title']")))
        success_title_text = success_title.text

        # Проводим проверку полученного значения с необходимым
        assert success_title_text == "Your Cart"
        print("Тест успешен")

        time.sleep(2)

        # Закрываем браузер
        self.driver.close()

# Создаем экземпляр класса, передаем url, которым будет взаимодействовать класс
tester = Test(base_url = "https://www.saucedemo.com/")

# Вызываем тест, указываем необходимые для авторизации данные пользователя
tester.test_login_and_adding_in_cart(username = "standard_user", password = "secret_sauce")