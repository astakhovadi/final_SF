import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
import requests


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(executable_path=r'D:/skillfactory/chromedriver.exe')
   yield
   pytest.driver.quit()


def test_ozon(): # Тестируем работоспособность ссылки
   url = "https://login.aliexpress.ru/"
   status = requests.get(url, params='').status_code
   assert status == 200


def test_valid_login(): # регистрация валидными логином и паролем
   # Ввоим ссылку на личный кабинет
   pytest.driver.get(
      'https://login.aliexpress.ru/?flag=1&return_url=https%3A%2F%2Ftrade.aliexpress.ru%2ForderList.htm%3Fspm%3Da2g2w.home.1000001.10.21cd501dj6F1TJ%26tracelog%3Dws_topbar%26_ga%3D2.133984070.936304568.1653134901-1302122509.1653134901')

   # Вводим логин
   pytest.driver.find_element_by_id('fm-login-id').send_keys('<valid_login>')
   # Вводим пароль
   pytest.driver.find_element_by_id('fm-login-password').send_keys('<valid_pass>')
   # Нажимаем на кнопку "Войти"
   pytest.driver.find_element_by_css_selector(
      'button[class="ali-kit_Button__button__18ub7i ali-kit_Button__size-l__18ub7i contained ali-kit_Button__primary__18ub7i batman-v2_index__login-submit__1a53tq"]').click()
   pytest.driver.implicitly_wait(5)  # неявное ожидание
   # Проверяем, что попали на нужную страницу
   assert pytest.driver.find_element_by_tag_name('h1').text == "Активные заказы"


def test_no_valid_login(): # при неверном вводе логина возникает сообщение "Ваши учетное имя или пароль неправильные."
   # Вводим email
   pytest.driver.get(
      'https://login.aliexpress.ru/?flag=1&return_url=https%3A%2F%2Ftrade.aliexpress.ru%2ForderList.htm%3Fspm%3Da2g2w.home.1000001.10.21cd501dj6F1TJ%26tracelog%3Dws_topbar%26_ga%3D2.133984070.936304568.1653134901-1302122509.1653134901')

   pytest.driver.find_element_by_id('fm-login-id').send_keys('pavelivanovich165')
   pytest.driver.find_element_by_id('fm-login-password').send_keys('123456')
   pytest.driver.find_element_by_css_selector(
      'button[class="ali-kit_Button__button__18ub7i ali-kit_Button__size-l__18ub7i contained ali-kit_Button__primary__18ub7i batman-v2_index__login-submit__1a53tq"]').click()
   pytest.driver.implicitly_wait(5)  # неявное ожидание
   assert pytest.driver.find_element_by_css_selector('span[class="batman-v2_index__fm-error-message__167xz7"]').text == "Ваши учетное имя или пароль неправильные."

def test_no_valid_pass():  #  при неверном вводе пароля возникает сообщение "Ваши учетное имя или пароль неправильные."

   pytest.driver.get(
      'https://login.aliexpress.ru/?flag=1&return_url=https%3A%2F%2Ftrade.aliexpress.ru%2ForderList.htm%3Fspm%3Da2g2w.home.1000001.10.21cd501dj6F1TJ%26tracelog%3Dws_topbar%26_ga%3D2.133984070.936304568.1653134901-1302122509.1653134901')

   # Вводим email

   pytest.driver.find_element_by_id('fm-login-id').send_keys('pavelivanovich165@yandex.ru')
   pytest.driver.find_element_by_id('fm-login-password').send_keys('1234')
   pytest.driver.find_element_by_css_selector(
         'button[class="ali-kit_Button__button__18ub7i ali-kit_Button__size-l__18ub7i contained ali-kit_Button__primary__18ub7i batman-v2_index__login-submit__1a53tq"]').click()
   pytest.driver.implicitly_wait(5)  # неявное ожидание
   assert pytest.driver.find_element_by_css_selector(
         'span[class="batman-v2_index__fm-error-message__167xz7"]').text == "Ваши учетное имя или пароль неправильные."

def test_no_pass():  #  при отсутствии пароля кнопка "Войти" не работает. Тест должен упасть
   pytest.driver.get(
      'https://login.aliexpress.ru/?flag=1&return_url=https%3A%2F%2Ftrade.aliexpress.ru%2ForderList.htm%3Fspm%3Da2g2w.home.1000001.10.21cd501dj6F1TJ%26tracelog%3Dws_topbar%26_ga%3D2.133984070.936304568.1653134901-1302122509.1653134901')

   # Вводим email
   pytest.driver.find_element_by_id('fm-login-id').send_keys('pavelivanovich165@yandex.ru')

   pytest.driver.find_element_by_css_selector(
         'button[class="ali-kit_Button__button__18ub7i ali-kit_Button__size-l__18ub7i contained ali-kit_Button__primary__18ub7i batman-v2_index__login-submit__1a53tq"]').click()
   assert pytest.driver.find_element_by_css_selector(
         'span[class="batman-v2_index__fm-error-message__167xz7"]').text == "Ваши учетное имя или пароль неправильные."



def test_product_card():# информация о товаре: наличие фото, описания, цены
   # Переходим на карточку товара
   pytest.driver.get('https://aliexpress.ru/item/1005003017556701.html?spm=a2g2w.productlist.0.0.10de18246yW79Z&sku_id=12000023251868258')
   # Проверяем наличие фото
   assert pytest.driver.find_elements_by_css_selector('img[class="ali-kit_Image__image__1jaqdj Product_Gallery__img__9bm18"]')[0].get_attribute('src') != ''
   # Проверяем наличие описания к товару
   assert pytest.driver.find_elements_by_css_selector(
      'h1[class="ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current"]')[0].text != ''
   # Проверяем наличие цены
   assert pytest.driver.find_element_by_css_selector(
'span[class="ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current"]')[0].text != ''




def test_Shopping_Cart(): # добавляем товар в корзину
   # Переходим в личный кабинет
   pytest.driver.get(
   'https://login.aliexpress.ru/?flag=1&return_url=https%3A%2F%2Ftrade.aliexpress.ru%2ForderList.htm%3Fspm%3Da2g2w.home.1000001.10.21cd501dj6F1TJ%26tracelog%3Dws_topbar%26_ga%3D2.133984070.936304568.1653134901-1302122509.1653134901')

   # Входим в свой аккаунт
   pytest.driver.find_element_by_id('fm-login-id').send_keys('<valid_login>')
   pytest.driver.find_element_by_id('fm-login-password').send_keys('<valid_pass>')
   pytest.driver.find_element_by_css_selector(
      'button[class="ali-kit_Button__button__18ub7i ali-kit_Button__size-l__18ub7i contained ali-kit_Button__primary__18ub7i batman-v2_index__login-submit__1a53tq"]').click()
   pytest.driver.implicitly_wait(5)  # неявное ожидание

   # Переходим на страницу товара и добавляем товар в корзину
   pytest.driver.get(
      'https://aliexpress.ru/item/1005003017556701.html?_ga=2.99837014.936304568.1653134901-1302122509.1653134901&mp=1&sku_id=12000023251868258&spm=a2g2w.cart.0.0.6bbe4aa6LubsS3')
   pytest.driver.find_element_by_css_selector('button[class="ali-kit_Button__button__18ub7i ali-kit_Button__size-l__18ub7i contained ali-kit_Button__warning__18ub7i Product_Actions__button__1j0pn"]').click()

   # Переходим в корзину
   pytest.driver.find_element_by_css_selector(
      'p[class="ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Paragraph__paragraph__1w2ua6 ali-kit_Paragraph__size-xs__1w2ua6 Product_CartPopupHeader__linkAsButtonText__1lfjs"]').click()
   result = pytest.driver.find_element_by_tag_name('h3').text
   # проверяем, что открыли корзину
   assert  "Корзина" in result
   # проверяем, что товар есть в корзине
   assert pytest.driver.find_elements_by_css_selector('a[class="ShoppingcartItemList_ProductCard__productNameLink__1nl31"]')[0].get_attribute('href')=="https://www.aliexpress.ru/item/1005003017556701.html?mp=1"

   #  Тестируем увеличение количества товара в корзине
   pytest.driver.find_elements_by_css_selector("svg[class='ali-icons_SvgIcon__icon__75ocax ali-icons_SvgIcon__size_M__75ocax ShoppingcartItemList_NumActionGroup__numIcon__ehpij']")[0].click()
   assert pytest.driver.find_elements_by_css_selector('input[class="ShoppingcartItemList_NumActionGroup__numInput__ehpij"]')[0].get_attribute('value')=="2"

   # Тестируем уменьшение количества товара в корзине
   pytest.driver.find_elements_by_css_selector("svg[class='ShoppingcartItemList_NumActionGroup__numIcon__ehpij']")[0].click()
   assert   pytest.driver.find_elements_by_css_selector('input[class="ShoppingcartItemList_NumActionGroup__numInput__ehpij"]')[0].get_attribute('value') == "1"

   #  Удаляем товар из корзины
   pytest.driver.find_element_by_css_selector("svg[class='ShoppingcartItemList_ControlActionGroup__actionIcon__xpegy']").click()
   # Смотрим, что товар отсутствует
   assert pytest.driver.find_elements_by_css_selector('a[class="ShoppingcartItemList_ProductCard__productNameLink__1nl31"]')[0].get_attribute('href') == "https://www.aliexpress.ru/item/1005003017556701.html?mp=1"


def test_search_by_name(): #  поиск товара и фильтрование товара# .
   #Открываем главную страницу
   pytest.driver.get(
      'https://best.aliexpress.ru/?spm=a2g2w.home.1000002.1.4918501dd3zhsW&_ga=2.95702228.936304568.1653134901-1302122509.1653134901')

   #  Ищем товар
   pytest.driver.find_element_by_name('SearchText').send_keys('stray kids'+ Keys.ENTER)
   assert pytest.driver.find_element_by_tag_name('h1').text == "stray kids"

   #  Фильтруем товар. Устанавливаем диапазон цен от 10 до 100 руб.
   pytest.driver.find_element_by_xpath("//input[@placeholder='мин']").send_keys('1'+ Keys.ENTER)
   pytest.driver.find_element_by_xpath("//input[@placeholder='макс']").send_keys('100'+ Keys.ENTER)

   pytest.driver.implicitly_wait(10)  # неявное ожидание
   # Записываем цены в массив, смотрим, что все цены в заданном диапазоне
   cost = pytest.driver.find_elements_by_css_selector('div[class="snow-price_SnowPrice__mainM__2y0jkd"]')
   for i in range(len(cost)):
      sum = str(cost[i].text).replace(',', '.')
      assert  float (sum[0]) <100

