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
base_url = "https://www.lambdatest.com/selenium-playground/upload-file-demo"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Путь к файлу, который надо сохранить
file_path = "C:\\Users\\user\\PycharmProjects\\SeleniumRefresh\\screenshots\\20251010-152134.png"
# Отдельно сохраним название в переменную
file_name = "20251010-152134.png"

# Находим локатор кнопки для загрузки файла
upload_file_button = driver.find_element(By.XPATH, "//input[@id='file']")
# Передаем путь к загружаемому файлу
upload_file_button.send_keys(file_path)
print("Файл загружен")

# Сохраняем название загруженного файла из элемента
file_name_from_site = upload_file_button.get_attribute("value")
file_name_from_site = file_name_from_site.replace("C:\\fakepath\\", "")
print(file_name_from_site)

# Проверка корректности
assert file_name_from_site == file_name
print("Файл загружен корректно")

time.sleep(2)

# Выход из браузера
driver.quit()