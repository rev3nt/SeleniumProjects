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
base_url = "https://demoqa.com/radio-button"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Находим чекбокс по лейблу
selected_radiobutton = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
# Извлекаем из лейбла текст для сравнения
selected_radiobutton_text = selected_radiobutton.text
# Нажимаем кнопку
selected_radiobutton.click()
# Извлекаем текст с результатом нажатия
selected_text = driver.find_element(By.XPATH, "//span[@class='text-success']").text
# Проверяем соответствует ли лейб выбранному значению
assert selected_text == selected_radiobutton_text
print("Выбран корректный radiobutton")

time.sleep(2)

# Закрываем браузер
driver.close()