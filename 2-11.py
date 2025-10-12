import time

from faker import Faker
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
base_url = "https://www.saucedemo.com"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Создаем объект класса фейкер, который будет генерировать данные на английском
fake = Faker("en_US")

# Генерируем username
username = fake.user_name()

# Находим локатор поля с логином и вставляем сгенерированные данные
username_input_field = driver.find_element(By.ID, "user-name")
username_input_field.send_keys(username)

time.sleep(3)

# Закрываем браузер
driver.close()