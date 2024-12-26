from bs4 import BeautifulSoup
import requests


def get_medicine_product_info(self):
    if 'zenyth.ro' in self.product_url:
        get_zenyth_info(self)
    else:
        self.price = 0

def get_zenyth_info(self):
    html = requests.get(self.product_url).text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find_all(class_='woocommerce-Price-amount')
    price = price[0].text
    price = price.split(',')[0] if price else None
    name = soup.find_all(class_='post_title')
    name = name[0].text if name else ''
    if not self.name:
        self.name = name
    self.price = int(price)

