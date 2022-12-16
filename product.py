import requests
from bs4 import BeautifulSoup


class Product:
    def __init__(self, url_link):
        self.url_link = url_link
        self.type = 'lxml'

    def init(self):
        html_text = requests.get(self.url_link).text
        return BeautifulSoup(html_text, 'lxml')

    def product_details(self):
        product = self.init().find('div', class_='product-container')
        return product.find('div', class_='container-right-content')

    def get_product_title(self):
        return self.product_details().find('h1', class_='pr-new-br').text

    def get_product_price(self):
        return self.product_details().find('div', class_='product-price-container').text

    def get_product_descriptions(self):
        descriptions = []
        for product_description in self.product_details().find('ul', id='content-descriptions-list').find_all('li'):
            descriptions.append(product_description.text)
        return descriptions

    def get_product_sizes(self):
        sizes = []
        for product_size in self.product_details().find_all('div', class_='sp-itm'):
            sizes.append(product_size.text)
        return sizes

    def get_product_images(self):
        images = []
        for product_image in self.product_details().find_all('a', class_='slc-img'):
            images.append(product_image.find('img')['src'])
        return images
