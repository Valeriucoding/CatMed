import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests


def get_medicine_product_info(self):
    if self.product_url:
        html = requests.get(self.product_url).text
        soup = BeautifulSoup(html, 'html.parser')
        domain = urlparse(self.product_url).netloc

        if 'zenyth.ro' in domain:
            _scrape_zenyth(self, soup)
        elif 'secom.ro' in domain:
            _scrape_secom(self, soup)
        elif 'drmax.ro' in domain:
            _scrape_drmax(self, soup)


def _scrape_zenyth(self, soup):
    """Set name and price from Zenyth website if found"""
    price_elem = soup.find(class_='woocommerce-Price-amount')
    if price_elem:
        price_text = price_elem.text.strip()
        price = price_text.split(',')[0]
        if price.isdigit():
            self.price = int(price)

    if not self.name:
        name_elem = soup.find(class_='post_title')
        if name_elem:
            self.name = name_elem.text.strip()


def _scrape_secom(self, soup):
    """Set name and price from Secom website if found"""
    price_elem = soup.find(class_='price-item')
    if price_elem:
        match = re.search(r'(\d+),\d+', price_elem.text)
        if match:
            self.price = int(match.group(1))

    if not self.name:  # Only set name if not already set
        name_elem = soup.find(class_='product-single__title')
        if name_elem:
            self.name = name_elem.text.strip()

def _scrape_drmax(self, soup):
    """Set name and price from Dr. Max website if found"""
    price_elem = soup.find(class_='price-text')
    if price_elem:
        price_text = price_elem.text.strip()
        try:
            self.price = float(price_text.replace(',', '.').replace(' Lei', ''))
        except ValueError:
            self.price = None

    if not self.name:
        name_elem = soup.find(class_='pr-detail__title')
        if name_elem:
            self.name = name_elem.text.strip()