import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


download_path = "C:\\Users\\user\\PycharmProjects\\SeleniumRefresh\\download_files\\"
# Настройки перед запуском браузера
options = webdriver.ChromeOptions()
# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)
# Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False,
                                          "download.default_directory": download_path})

# Создание экземпляра драйвера с автоматической установкой последней версии
driver = webdriver.Chrome(options=options)
# Базовый url, с которым взаимодействует скрипт
base_url = "https://www.lambdatest.com/selenium-playground/download-file-demo"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
download_button.click()

file_name = "LambdaTest.pdf"
file_path = download_path + file_name

time.sleep(2)

assert os.access(file_path, os.F_OK) == True
print("Файл скачен")

files = glob.glob(os.path.join(download_path, "*.*"))
for file in files:
    file_size = os.path.getsize(file)
    if file_size > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")

time.sleep(4)

for file in files:
    os.remove(file)