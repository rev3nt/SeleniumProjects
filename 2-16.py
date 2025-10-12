import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


download_path = "C:\\Users\\user\\PycharmProjects\\SeleniumRefresh\\download_files\\"
# Настройки перед запуском браузера
options = webdriver.ChromeOptions()
# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)
# Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

# Создание экземпляра драйвера с автоматической установкой последней версии
driver = webdriver.Chrome(options=options)
# Базовый url, с которым взаимодействует скрипт
base_url = "https://demoqa.com/dynamic-properties"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

try:
# Получаем локатор невидимой кнопки и пытаемся нажать на нее
    invisible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    invisible_button.click()
# Ловим исключение
except NoSuchElementException:
    print("Элемента нет на странице")

# Перезагружаем страницу
    driver.refresh()

# Ожидаем 5 секунд
    time.sleep(5)

# Снова получаем локатор кнопки
    invisible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    invisible_button.click()
    print("Кнопка была успешно нажата!")

    time.sleep(3)

# Закрываем браузер
    driver.quit()