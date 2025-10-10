import time

from selenium import webdriver
from selenium.webdriver.common.by import By


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

# Сохраняем поле ввода пароля в переменную
password = driver.find_element(By.XPATH, "//input[@id='password']")
# Вводим неверный пароль в поле
password.send_keys("secret_sauce")
print("Пароль введен")

# Находим кнопку логина по локатору
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
# Нажимаем кнопку логина
login_button.click()
print("Кнопка логина нажата")

#Нажимаем на кнопку скрытого меню
sidebar_menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
sidebar_menu_button.click()
print("Меню раскрыто")

#Ожидание окончания анимации развертывания меню
time.sleep(1)

# Нажимаем на кнопку, чтобы разлогиниться
sidebar_logout_button = driver.find_element(By.ID, "logout_sidebar_link")
sidebar_logout_button.click()
print("Пользователь успешно разлогинен")

time.sleep(2)

# Закрываем браузер
driver.close()