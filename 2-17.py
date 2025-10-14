import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
base_url = "https://www.saucedemo.com/"

fake = Faker()

menu_dict = {'1': 'Sauce Labs Backpack', '2': "Sauce Labs Bike Light", '3': "Sauce Labs Bolt T-Shirt",
             '4': "Sauce Labs Fleece Jacket", '5': "Sauce Labs Onesie", '6': 'Test.allTheThings() T-Shirt (Red)")”'}

print("Выберете опцию из меню")

# Выводим пользовательское меню
for item in menu_dict:
    print(f'{item}: {menu_dict[item]}')

# Просим ввод до момента, пока не будет выбрана валидная опция
while True:
    user_input = input("Выбери один из следующих товаров и укажи его номер: ")

    if user_input not in menu_dict:
        print("Вы ввели некорректную опцию")
    else:
        break

# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Вводим логин
login_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user-name")))
login_field.send_keys('standard_user')

# Вводим пароль
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
password_field.send_keys('secret_sauce')

# Логинимся
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# Сохраняем выбор пользователя, он будет использоваться для проведения тестов
users_choice = menu_dict[user_input]

print(f'Выбрана опция {users_choice}')

# Находим карточку товара по названию товара, находим цену из контейнера с товаром
product_container = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{users_choice}']/ancestor::div[@class='inventory_item_description']")))
product_price = product_container.find_element(By.CLASS_NAME, "inventory_item_price").text
print(f'Цена выбранного товара: {product_price}')

# Находим в контейнере кнопку для добавления в корзине
add_to_cart_button = product_container.find_element(By.XPATH, ".//button[contains(text(), 'Add to cart')]")
add_to_cart_button.click()
print("Товар добавлен в корзину")

time.sleep(2)

# Переходим в корзину
cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
cart_button.click()
print("Переход в корзину")

# Извлекаем информацию о товаре в корзине
cart_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_name']"))).text
cart_price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_price']"))).text
print(cart_title)
print(cart_price)

# Сверяем с данными, введенными пользователем и указанными на главной странице
assert cart_title == users_choice
assert cart_price == product_price
print("Содержимое корзины соответствует пользовательскому выбору")

time.sleep(2)

# Переходим на страницу доставки
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()

# Генерируем данные о пользователе
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postcode()

# Находим локаторы полей для ввода данных
first_name_filed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='first-name']")))
last_name_filed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='last-name']")))
postal_code_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='postal-code']")))

# Вводим сгенерированные данные
first_name_filed.send_keys(first_name)
last_name_filed.send_keys(last_name)
postal_code_field.send_keys(postal_code)

time.sleep(2)

# Переходим на страницу обзора заказа
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
print("Переход на страницу с обзором заказа")

# Находим поля с названием, ценой и ценой заказа без налога
checkout_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_name']"))).text
checkout_price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_price']"))).text
total_price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='summary_subtotal_label']"))).text
total_price = total_price.replace('Item total: ', '')

# Проверяем на соответствие оригинальным данным
assert checkout_title == users_choice
assert checkout_price == product_price
assert total_price == product_price
print("Информация о заказе в обзоре соответствует выбранным опциям")

time.sleep(2)

# Подтверждаем заказ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))).click()

# Сохраняем сообщение об успешном оформлении заказа
complete_text = 'Thank you for your order!'

# Ищем сообщение на странице
complete_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[contains(text(), '{complete_text}')]"))).text

# Подтверждаем успешность созданного заказа
assert complete_title == complete_text
print("Тест успешен")

time.sleep(3)

# Выходим из браузера
driver.quit()