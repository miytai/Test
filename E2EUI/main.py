from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка веб-драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Открытие страницы входа
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Ввод данных для входа
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()


    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_container")))

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    print('good')


    cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_button.click()

    # Проверка, что товар добавлен в корзину
    cart_items = driver.find_elements(By.CLASS_NAME, "cart-list")
    item_names = [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in cart_items]

    checkout_button = driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']")
    checkout_button.click()
    # Ожидание загрузки страницы оформления заказа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "checkout_info")))

    # Заполнение данных заказа
    first_name_input = driver.find_element(By.NAME, "firstName")
    last_name_input = driver.find_element(By.NAME, "lastName")
    zip_code_input = driver.find_element(By.NAME, "postalCode")

    # Ввод данных
    first_name_input.send_keys("Имя")  # Замените "Имя" на нужное
    last_name_input.send_keys("Фамилия")  # Замените "Фамилия" на нужное
    zip_code_input.send_keys("12345")  # Замените "12345" на нужный почтовый индекс

    # Нажимаем кнопку Continue
    continue_button = driver.find_element(By.CSS_SELECTOR, "[data-test='continue']")
    continue_button.click()
    continue_button = driver.find_element(By.CSS_SELECTOR, "[data-test='finish']")
    continue_button.click()
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    if "Thank you for your order!" in success_message:
        print("Заказ оформлен успешно:", success_message)




finally:
    time.sleep(2)
    driver.quit()
