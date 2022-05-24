#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://best.aliexpress.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='downshift-134913-input')

    # Search button
    search_run_button = WebElement(xpath='//button[@class="Header_SearchSection__searchButton__1cpwf"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//div[contains(@href, "/product-")]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[class="SearchMainFilters_SortButtons__buttonSelected__vjh8h"]')

