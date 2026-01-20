import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    """Вычисляет значение функции для капчи"""
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Шаг 1: Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    print("Открыта страница бронирования дома")
    print(f"Текущий URL: {browser.current_url}")
    
    # Шаг 2: Ждем, когда цена уменьшится до $100
    # Создаем объект явного ожидания с таймаутом 15 секунд
    wait = WebDriverWait(browser, 15)
    
    print("Ожидаем снижения цены до $100...")
    print("Текущая цена:", browser.find_element(By.ID, "price").text)
    
    # Используем условие text_to_be_present_in_element
    # Оно проверяет, содержит ли элемент указанный текст
    price_condition = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    
    # Ждем выполнения условия
    # Метод until возвращает элемент, когда условие выполнено
    price_element = wait.until(price_condition)
    
    print(f"Ура! Цена снизилась до: {browser.find_element(By.ID, 'price').text}")
    
    # Шаг 3: Нажимаем на кнопку "Book"
    # Кнопка становится активной только при цене $100
    book_button = browser.find_element(By.ID, "book")
    
    # Проверяем, что кнопка доступна для клика
    if book_button.is_enabled():
        print("Нажимаем кнопку Book...")
        book_button.click()
    else:
        print("Кнопка Book неактивна!")
        raise Exception("Кнопка Book недоступна для клика")
    
    # Шаг 4: Решаем математическую задачу
    # Даем время для появления формы с заданием
    time.sleep(1)
    
    # Получаем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x_value = x_element.text
    print(f"Получено значение x: {x_value}")
    
    # Вычисляем результат
    result = calc(x_value)
    print(f"Результат вычислений: {result}")
    
    # Вводим ответ в поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result)
    print("Ответ введен в поле")
    
    # Шаг 5: Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    print("Форма отправлена")
    
    # Шаг 6: Получаем финальный результат
    # Ждем появления алерта
    time.sleep(2)
    
    final_alert = browser.switch_to.alert
    final_result = final_alert.text
    print(f"Финальный результат: {final_result}")
    
    # Извлекаем только число из текста алерта
    answer_number = final_result.split()[-1]
    print(f"Число для ответа: {answer_number}")
    
    # Закрываем алерт
    final_alert.accept()
    
except Exception as e:
    print(f"Ошибка во время выполнения: {type(e).__name__}: {str(e)}")
    
finally:
    # Даем время увидеть результат перед закрытием
    time.sleep(3)
    browser.quit()