import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
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
base_url = "https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Создаем объект select в который поместим локатор необходимого дропдаун меню
select = Select(driver.find_element(By.XPATH, "//select[@class='select2-hidden-accessible']"))
# Выбираем пункт в меню по значению
select.select_by_value("India")

time.sleep(2)

# Закрываем браузер
driver.close()