import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys
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
base_url = "https://demoqa.com/date-picker"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Формируем дату на 10 дней позже текущей
future_date = datetime.date.today() + datetime.timedelta(days=10)
# Форматируем ее в строку, чтобы записать в поле
future_date = future_date.strftime("%m.%d.%Y")

# Находил локатор поля ввода даты
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# Удаляем текущую информацию из поля
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)
# Вписываем сформированную ранее дату
date_input.send_keys(future_date)

time.sleep(4)

# Закрываем браузер
driver.close()