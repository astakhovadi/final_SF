# Run tests:    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#

import pytest
from pages.ozon import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)
# Задаем строку поиска
    page.search = 'stray kids'
    page.search_run_button.click()

    # Проверяем, что найдены товары по запросу:
    assert page.products_titles.count() > 0
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'stray kids' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Ищем товары с неверной раскладкой
    page.search = 'ыекфн лшвы'
    page.search_run_button.click()

    # Проверяем, что найдены товары по запросу:
    assert page.products_titles.count() > 0
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'stray kids' in title.lower(), msg


def test_check_mistake_input_in_search(web_browser):
    """ Make sure that the misspelled name input is working fine. """

    page = MainPage(web_browser)

    # Ищем товары с опечаткой в запросе:
    page.search = 'stra klds'
    page.search_run_button.click()

    assert page.products_titles.count() > 0
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'stray kids' in title.lower(), msg

