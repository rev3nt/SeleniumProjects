import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
user_name.send_keys("standard_user!@#")
print("Логин введен")

# Сохраняем поле ввода пароля в переменную
password = driver.find_element(By.XPATH, "//input[@id='password']")
# Вводим неверный пароль в поле
password.send_keys("secret_sauce3112")
print("Пароль введен")

time.sleep(2)

# Выделяем текст в поле логин и удаляем содержимое
user_name.send_keys(Keys.CONTROL + 'a')
user_name.send_keys(Keys.DELETE)
# Выделяем текст в поле пароль и удаляем содержимое
password.send_keys(Keys.CONTROL + 'a')
password.send_keys(Keys.DELETE)

time.sleep(2)

# Вводим корректные логин и пароль
user_name.send_keys("standard_user")
print('Логин введен')
password.send_keys("secret_sauce")
print('пароль введен')

time.sleep(2)

# Находим кнопку логина по локатору
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
# Нажимаем кнопку логина
login_button.click()

time.sleep(2)

# Закрываем браузер
driver.close()