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
base_url = "https://www.lambdatest.com/selenium-playground/simple-form-demo"
# Открытие ссылки в браузере
driver.get(base_url)
# Развертывание окна браузера на полный экран
driver.maximize_window()

# Создаем тестовое сообщение для проверки поля
test_message = 'This is a test message'

time.sleep(3)

# Находим поле по локатору и вводим туда заготовленный текст
text_input_field = driver.find_element(By.XPATH, "//input[@id='user-message']")
text_input_field.send_keys(test_message)

# Нажимаем на кнопку, которая должна вывести текст из поля на экран
get_checked_value_button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
get_checked_value_button.click()

# Находим сообщение по локатору и извлекаем из него текст
message_from_site = driver.find_element(By.XPATH, '//p[@id="message"]').text

# Делаем сравнение с оригинальным текстом
assert message_from_site == test_message
print("Сообщение успешно отправлено")

# Создаем сумму из двух чисел
first_sum_value = 52
second_sum_value = 42
control_summ = first_sum_value + second_sum_value

# Находим поля ввода для этих двух чисел
first_value_input = driver.find_element(By.XPATH, '//input[@id="sum1"]')
second_value_input = driver.find_element(By.XPATH, '//input[@id="sum2"]')

# Вводим их в поля
first_value_input.send_keys(str(first_sum_value))
second_value_input.send_keys(str(second_sum_value))

# Нажимаем на кнопку, которая должна посчитать сумму
get_sum_button = driver.find_element(By.XPATH, '//button[contains(text(), "Get Sum")]')
get_sum_button.click()

# Извлекаем сумму, которую посчитал сайт
site_summ = driver.find_element(By.XPATH, '//p[@id="addmessage"]').text

# Делаем сравнение с суммой сформированной изначально
assert site_summ == str(control_summ)
print("Сумма вычислена корректно")