import time

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
base_url = "https://demoqa.com/buttons"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Добавляем экземпляр класса для выполнения двойного клика и клика правой кнопкой мыши
actions = ActionChains(driver)

# Находим локатор кнопка для дабл клика
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# Делаем двойной клик по кнопке
actions.double_click(double_click_button).perform()
print("Double click button")

time.sleep(2)

# Находим локатор кнопка для клика правой кнопкой мыши
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# Делаем двойной клик по кнопке
actions.context_click(right_click_button).perform()
print("Right click button")

time.sleep(2)

# Закрываем браузер
driver.close()