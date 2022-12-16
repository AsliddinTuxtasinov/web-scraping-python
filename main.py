import json
from product import Product


url = 'https://www.trendyol.com/altinyildiz-classics/erkek-beyaz-slim-fit-bis' \
      'iklet-yaka-100-pamuk-kisa-kollu-tisort-p-224555799'

product = Product(url_link=url)

# Data to be written
dictionary = {
      "product_title": product.get_product_title(),
      "product_price": product.get_product_price(),
      "product_descriptions": product.get_product_descriptions(),
      "product_sizes": product.get_product_sizes(),
      "product_images": product.get_product_images()
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)


# Writing to sample.json
def save_date(data):
    with open("data.json", "w") as file:
        file.write(data)
    print("data saved")


if __name__ == '__main__':
    save_date(json_object)
