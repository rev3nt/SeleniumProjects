import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def __init__(self, base_url):
        self.base_url = base_url

    def init_chrome_driver(self):
        # Настройки перед запуском браузера
        options = webdriver.ChromeOptions()
        # Опция, позволяющая сохранять браузер открытым после выполнения скрипта
        options.add_experimental_option('detach', True)
        # Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
        options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

        # Инициализируем драйвер для взаимодействия с браузером
        self.driver = webdriver.Chrome(options=options)

    def test_login_page_positive(self, username, password):
        # Открытие ссылки в браузере
        self.driver.get(self.base_url)
        # Развертывание окна браузера на полный экран
        self.driver.maximize_window()

        # Сохраняем поле ввода логина в переменную
        user_name_input = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        # Вписываем неверный логин в поле
        user_name_input.send_keys(username)
        print("Логин введен")

        time.sleep(1)

        # Сохраняем поле ввода пароля в переменную
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # Вводим неверный пароль в поле
        password_input.send_keys(password)
        print("Пароль введен")

        time.sleep(1)

        # Находим кнопку логина по локатору
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        # Нажимаем кнопку логина
        login_button.click()
        print("Кнопка логина нажата")

        time.sleep(2)
        # Находим сообщение на странице корзины
        products_title_text = self.driver.find_element(By.XPATH, '//span[@class="title"]').text

        # Проверяем его содержимое на правильность
        assert products_title_text == "Products"
        print("Тест прошел успешно")

        # Закрываем браузер
        self.driver.close()


# Создаем экземпляр класса, передаем url, которым будет взаимодействовать класс
tester = Test(base_url = "https://www.saucedemo.com/")

# Инициализируем драйвер для необходимого браузера
tester.init_chrome_driver()

# Вызываем тест, указываем необходимые для авторизации данные пользователя
tester.test_login_page_positive(username = "standard_user", password = "secret_sauce")