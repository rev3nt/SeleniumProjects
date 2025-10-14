import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


class Test:
    def test_login_and_adding_in_cart(self):
        # Настройки перед запуском браузера
        options = webdriver.ChromeOptions()
        # Опция, позволяющая сохранять браузер открытым после выполнения скрипта
        options.add_experimental_option('detach', True)
        # Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
        options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

        # Создание экземпляра драйвера с автоматической установкой последней версии
        driver = webdriver.Chrome(options=options)
        # Базовый url, с которым взаимодействует скрипт
        base_url = "https://www.saucedemo.com/"
        # Открытие ссылки в браузере
        driver.get(base_url)
        # Развертывание окна браузера на полный экран
        driver.maximize_window()

        # Добавляем экзмепляр класса из модуля для проведения логина на сайт
        login_page = LoginPage(driver)
        # Вызываем метод логина для стандартного пользователя
        login_page.login(username="standard_user", password="secret_sauce")

        # Добавляем товар в корзину
        add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        print("Товар добавлен в корзину")

        # Переходим на страницу корзины
        go_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        go_cart_button.click()
        print("Переход в корзину")

        # Находим текст, с которым будем сверяться, успешен ли переход на страницу корзины или нет
        success_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='title']")))
        success_title_text = success_title.text

        # Проводим проверку полученного значения с необходимым
        assert success_title_text == "Your Cart"
        print("Тест успешен")

        time.sleep(2)

        # Закрываем браузер
        driver.close()


# Создаем экземпляр класса теста
tester = Test()

# Запускаем метод, который отвечает за проведения теста
tester.test_login_and_adding_in_cart()