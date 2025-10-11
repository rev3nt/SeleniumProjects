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
base_url = "https://demoqa.com/checkbox"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Находим чекбокс
home_checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
# Нажимаем на чекбокс
home_checkbox.click()

time.sleep(1)

# Проверяем, нажат ли чекбокс по состоянию скрытого элемента
checkbox_status = driver.find_element(By.XPATH, "//input[@id='tree-node-home']")

assert checkbox_status.is_selected()
print("Чекбокс выбран успешно")

# Закрываем браузер
driver.close()