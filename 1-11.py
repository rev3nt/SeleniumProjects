import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Настройки перед запуском браузера
options = webdriver.ChromeOptions()
# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)

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
# Вписываем логин в поле
user_name.send_keys("standard_user")
print("Логин введен")

# Сохраняем поле ввода пароля в переменную
password = driver.find_element(By.XPATH, "//input[@id='password']")
# Вводим пароль в поле
password.send_keys("secret_sauce")
print("Пароль введен")

time.sleep(2)

# Нажимаем Enter, чтобы залогиниться
password.send_keys(Keys.ENTER)

# Ожидаем полной подгрузки страницы
time.sleep(2)

# Формируем название скриншота страницы вместе с форматом
screenshot_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"
# Сохраняем скриншот в директорию
driver.save_screenshot("C:\\Users\\user\\PycharmProjects\\SeleniumRefresh\\screenshots\\" + screenshot_name)

# Закрываем браузер
driver.close()