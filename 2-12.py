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
base_url = "https://demoqa.com/browser-windows"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Находим локатор кнопки создания новой вкладки и нажимаем на нее
new_tab_button = driver.find_element(By.XPATH, '//button[@id="tabButton"]')
new_tab_button.click()

time.sleep(1)

# Меняем вкладку на первую
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

# Находим локатор кнопки создания нового окна и нажимаем на нее
new_window_button = driver.find_element(By.XPATH, '//button[@id="windowButton"]')
new_window_button.click()

time.sleep(1)

# Переходим в оригинальное окно
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

# Закрываем браузер
driver.quit()