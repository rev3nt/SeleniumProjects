import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Настройки перед запуском браузера
options = webdriver.ChromeOptions()

# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)

# Добавляем опцию запуска теста, без запуска самого браузера
#options.add_argument('--headless')

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
password.send_keys("УЭЭЭЭЭ")

print("Пароль введен")

# Выделяем все символы в поле с логином
user_name.send_keys(Keys.CONTROL + 'a')

time.sleep(1)

# Нажимаем кнопку удаления
user_name.send_keys(Keys.DELETE)

time.sleep(1)

# Выделяем все символы в поле с паролем
password.send_keys(Keys.CONTROL + 'a')

time.sleep(1)

# Нажимаем кнопку удаления
password.send_keys(Keys.DELETE)

time.sleep(1)

# Нажимаем Enter, чтобы залогиниться
password.send_keys(Keys.ENTER)

time.sleep(2)

# Закрываем браузер
driver.close()