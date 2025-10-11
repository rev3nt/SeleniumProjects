import time

from selenium import webdriver
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
base_url = "https://www.saucedemo.com/"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Сохраняем поле ввода логина в переменную
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# Вписываем неверный логин в поле
user_name.send_keys("standard_user")
print("Логин введен")

# Сохраняем поле ввода пароля в переменную
password = driver.find_element(By.XPATH, "//input[@id='password']")
# Вводим неверный пароль в поле
password.send_keys("secret_sauce")
print("Пароль введен")

# Находим кнопку логина по локатору
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
# Нажимаем кнопку логина
login_button.click()
print("Кнопка логина нажата")

# Сохраняем название и цену первого товара
product_1_title = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
print(product_1_title)
product_1_price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div").text
print(product_1_price)
# Добавляем первый товар в корзину
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
print("Первый товар добавлен в корзину")

# Сохраняем название и цену второго товара
product_2_title = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print(product_2_title)
product_2_price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div").text
print(product_2_price)
# Добавляем второй товар в корзину
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
print("Второй товар добавлен в корзину")

# Переходим на страницу корзины
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
print("Переход в корзину")

# Находим название и цену первого товара в корзине
cart_product_1_title = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
cart_product_1_price = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
# Сравниваем корректность отображения первого добавленного товара с исходными данными
assert cart_product_1_title == product_1_title
assert cart_product_1_price == product_1_price
print("Информация о первом товаре корректна")

# Находим название и цену второго товара в корзине
cart_product_2_title = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
cart_product_2_price = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
# Сравниваем корректность отображения второго добавленного товара с исходными данными
assert cart_product_2_title == product_2_title
assert cart_product_2_price == product_2_price
print("Информация о втором товаре корректна")

# Переходим на страницу оформления заказа
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
print("Переход на страницу оформления заказа")

# Вводим имя, фамилию и почтовый индекс в форму для оформления доставки
checkout_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
checkout_name.send_keys("Mihail")
checkout_lastname= driver.find_element(By.XPATH, "//*[@id='last-name']")
checkout_lastname.send_keys("Merkulov")
checkout_post_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
checkout_post_code.send_keys("123456")
print("Данные о получателе введены")

# Переходим на страницу c обзором заказа
driver.find_element(By.XPATH, "//*[@id='continue']").click()
print("Переход на страницу с обзором заказа")

# Извлекаем название и цену первого товара и сравниваем с оригинальными данными
checkout_product_1_title = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
checkout_product_1_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
assert checkout_product_1_title == product_1_title
assert checkout_product_1_price == product_1_price
print("Информация о первом товаре на странице оформления корректна")

# Извлекаем название и цену второго товара и сравниваем с оригинальными данными
checkout_product_2_title = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
checkout_product_2_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
assert checkout_product_2_title == product_2_title
assert checkout_product_2_price == product_2_price
print("Информация о втором товаре на странице оформления корректна")

# Рассчитываем цену всего заказа
total_price = float(checkout_product_1_price[1:]) + float(checkout_product_2_price[1:])
# Формируем строку, с которой будем сравнить элемент на сайте
formatted_total_price = "Item total: $" + str(total_price)

# Извлекаем элемент с финальной стоимостью и сравниваем с подсчитанной в программе
total_cart_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
assert total_cart_price.text == formatted_total_price
print("Финальная цена заказа рассчитана корректно")

# Подтверждаем заказ
driver.find_element(By.XPATH, "//*[@id='finish']").click()
print("Нажата кнопка подтверждения заказа")

# Проверяем удачно ли оформлен заказ по сравнению с сообщением об удачном проведении операции
complete_order_text = "Thank you for your order!"
complete_order_text_from_site = driver.find_element(By.XPATH, f"//*[contains(text(), '{complete_order_text}')]")
assert complete_order_text_from_site.text == complete_order_text
print("Заказ удачно оформлен")

time.sleep(2)

# Закрываем браузер
driver.close()