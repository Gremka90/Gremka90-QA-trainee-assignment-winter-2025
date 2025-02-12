from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import requests


# Иницилизация дравера
@pytest.fixture(autouse=True)
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

# Setup - Создание объявления, teardown - удаление тестового объявления.\
# Данные получаю параметризированно из теста
@pytest.fixture
def create_test_data(request):
    # Получаем данные из параметра теста
    test_data = request.param
    # Создание данных через API
    url = "http://tech-avito-intern.jumpingcrab.com/api/advertisements/"
    response = requests.post(url, json=test_data)
    test_data_id = response.json().get("id")

    # Передача ID в тест
    yield test_data_id

    # Удаление данных после завершения теста
    delete_url = f"http://tech-avito-intern.jumpingcrab.com/api/advertisements/{test_data_id}"
    delete_status =  requests.delete(delete_url)
    assert delete_status.status_code == 200
