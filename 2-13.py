import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Настройки перед запуском браузера
options = webdriver.ChromeOptions()
# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)
# Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

# Создание экземпляра драйвера с автоматической установкой последней версии
driver = webdriver.Chrome(options=options)
# Базовый url, с которым взаимодействует скрипт
base_url = "https://the-internet.herokuapp.com/javascript_alerts"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Создаем локатор кнопки с алертом и нажимаем на нее
alert_button = driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]')
alert_button.click()
time.sleep(1)
# Принимаем алерт
driver.switch_to.alert.accept()

time.sleep(2)

# Создаем локатор кнопки с алертом и нажимаем на нее
alert_button = driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]')
alert_button.click()
time.sleep(1)
# Отклоняем алерт
driver.switch_to.alert.dismiss()

time.sleep(2)

# Создаем локатор кнопки с алертом и нажимаем на нее
alert_button = driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]')
alert_button.click()
time.sleep(1)
# Вписываем промт
driver.switch_to.alert.send_keys("Funny monkey")
# Принимаем алерт
driver.switch_to.alert.accept()

time.sleep(2)

# Закрываем браузер
driver.quit()