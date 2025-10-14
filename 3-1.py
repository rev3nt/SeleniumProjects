import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def test_login_page_positive(self):
        # Настройки перед запуском браузера
        options = webdriver.ChromeOptions()
        # Опция, позволяющая сохранять браузер открытым после выполнения скрипта
        options.add_experimental_option('detach', True)
        #Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
        options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

        # Создание экземпляра драйвера с автоматической установкой последней версии
        driver = webdriver.Chrome(options=options)
        # Базовый url, с которым взаимодействует скрипт
        base_url = "https://www.saucedemo.com/"
        # Открытие ссылки в браузере
        driver.get(base_url)
        # Развертывание окна браузера на полный экран
        driver.maximize_window()

        # Сохраняем поле ввода логина в переменную
        user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
        # Вписываем неверный логин в поле
        user_name.send_keys("standard_user")
        print("Логин введен")

        time.sleep(1)

        # Сохраняем поле ввода пароля в переменную
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        # Вводим неверный пароль в поле
        password.send_keys("secret_sauce")
        print("Пароль введен")

        time.sleep(1)

        # Находим кнопку логина по локатору
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        # Нажимаем кнопку логина
        login_button.click()
        print("Кнопка логина нажата")

        time.sleep(2)

        products_title_text = driver.find_element(By.XPATH, '//span[@class="title"]').text

        assert products_title_text == "Products"
        print("Логин прошел успешно")

        # Закрываем браузер
        driver.close()


# Создаем экземпляр класса
tester = Test()

# Вызываем метод класса с тестом
tester.test_login_page_positive()