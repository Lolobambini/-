from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('40222505@mail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('123')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_my_pets():
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ', ' in descriptions[i]
       parts = descriptions[i].text.split(", ")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0


@pytest.fixture(autouse=True)
def testing(driver=True):
   pytest.driver = webdriver.Chrome('C:/drv/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')
   element = WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.ID, "myDynamicElement")))

   yield

   pytest.driver.quit()

# def test_check_photo_presence_my_pets():
#    stat=pytest.driver.find_element_by_css_selector('.\\.col-sm-4 left')
#    number = stat[0].text.split('/n')
#    number = number[1].split('')
#    number = int(number[1])
#    rows = pytest.driver.find_elements_by_css_selector('.table table-hover tr')
#
#    assert number == len(rows) - 1
#    driver = webdriver.Chrome()
#    driver.implicitly_wait(10)  # seconds
#    driver.get("http://somedomain/url_that_delays_loading")

#
