import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Настройки перед запуском браузера
options = webdriver.ChromeOptions()
# Опция, позволяющая сохранять браузер открытым после выполнения скрипта
options.add_experimental_option('detach', True)
#Отключение всплывающего окна с уведомлением о том, что введенный пароль есть в слитых базах данных
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

# Создание экземпляра драйвера с автоматической установкой последней версии
driver = webdriver.Chrome(options=options)
# Базовый url, с которым взаимодействует скрипт
base_url = "https://www.saucedemo.com/"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Сохраняем поле ввода логина в переменную
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# Вписываем логин в поле
user_name.send_keys("standard_user")
print("Логин введен")

# Сохраняем поле ввода пароля в переменную
password = driver.find_element(By.XPATH, "//input[@id='password']")
# Вводим пароль в поле
password.send_keys("secret_sauce")
print("Пароль введен")

# Нажимаем Enter, чтобы залогиниться
password.send_keys(Keys.ENTER)

# Ожидаем полной подгрузки страницы
time.sleep(1)

# Добавляем все товары в корзину
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()

# Переходим в корзину
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

# Создание объекта с действиями
action = ActionChains(driver)
# Локатор элемента, к которому необходимо проскролить
last_element_in_cart = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
# Перемещение по локатору
action.move_to_element(last_element_in_cart).perform()

time.sleep(2)

# Закрываем браузер
driver.close()