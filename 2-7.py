import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
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
base_url = "https://html5css.ru/howto/howto_js_rangeslider.php"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

actions = ActionChains(driver)

slider = driver.find_element(By.XPATH, "//input[@class='slider-square']")
time.sleep(2)

actions.click_and_hold(slider).move_by_offset(650, 0).release().perform()

slider_value = driver.find_element(By.XPATH, "//span[@id='f']").text

assert slider_value == '100'
print("Слайдер был сдвинут максимально вправо!")

time.sleep(2)

# Закрываем браузер
driver.close()