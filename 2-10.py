import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Настройки перед запуском браузера
options = webdriver.ChromeOptions()
# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)
# Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

# Создание экземпляра драйвера с автоматической установкой последней версии
driver = webdriver.Chrome(options=options)
# Базовый url, с которым взаимодействует скрипт
base_url = "https://www.lambdatest.com/selenium-playground/iframe-demo/"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

time.sleep(3)

# Находим iframe по локатору и переключаемся на него
iframe = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
driver.switch_to.frame(iframe)

# Формируемы тестовый текст, который будет введен в iframe
input_text = "New text for test!"

# Заменяем текст в iframe на подготовленный
iframe_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')
iframe_input.send_keys(Keys.CONTROL + "a")
time.sleep(1)
iframe_input.send_keys(input_text)

# Выделяем вписанный текст
iframe_input.send_keys(Keys.CONTROL + "a")
time.sleep(1)

# Находим локатор кнопки, чтобы сделать текст курсивным и нажимаем на кнопку
bold_button = driver.find_element(By.XPATH, '//button[@title="Italic"]')
bold_button.click()

# Извлекаем текст из iframe после редактирования
iframe_bold_text = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/b').text

# Сравниваем текст с исходным
assert iframe_bold_text == input_text
print("Редактирование прошло успешно")