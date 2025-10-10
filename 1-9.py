import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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
user_name = driver.find_element(By.XPATH, "//input[@id='password']")

# Вводим пароль в поле
user_name.send_keys("УЭЭЭЭЭ")

print("Пароль введен")

# Сохраняем кнопку для логина
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Нажимаем кнопку
login_button.click()

print("Кнопка входа нажата")

# URL для сравнения с результатом нажатии кнопки
test_url = "https://www.saucedemo.com/inventory.html"

# Получаем текущий URL
get_url = driver.current_url

# Проверяем на соответствие
assert test_url != get_url

print("Страница не открылась")

# Текст ошибки со страницы
test_text = "Epic sadface: Username and password do not match any user in this service"

# Ищем этот элемент на страницу и извлекаем из него текст
get_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

print(get_text)

# Проверяем появилось ли сообщение об ошибке
assert test_text == get_text

print("Ошибка успешно появилась")

# Помещаем кнопку закрывания ошибки в переменную
close_error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")

# Нажатие на кнопку закрытия ошибки
close_error_button.click()

print("Кнопка закрывания ошибки была успешно нажата")

# Ждем 2 секунды
time.sleep(2)

# Обновляем страницу, чтобы обновить поля ввода
driver.refresh()

# Ждем 3 секунды
time.sleep(3)

# Закрываем браузер
driver.close()