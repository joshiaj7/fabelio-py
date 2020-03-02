import requests
import re
from .models import Product
from bs4 import BeautifulSoup
from django.http import Http404


def clean_html_tag(text):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", text)
    return cleantext


def parse_and_insert(url):
    result = requests.get(url)

    if result.status_code == 404:
        raise Http404("Given URL not exist")

    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "lxml")
        desc = soup.find(id="description")
        price = soup.find_all("span", class_="price")[0]
        product_name = soup.find_all("span", class_="base")[0]
        image_div = soup.find_all("div")

        image = ""
        for item in image_div:
            if item.get("href") and "m2fabelio.imgix.net" in item.get("href"):
                image = str(item.get("href"))
                break

        desc = clean_html_tag(str(desc))
        price = int("".join(re.findall(r"\d+", str(price))))
        product_name = clean_html_tag(str(product_name))

        Product.objects.create(
            link_str=url, name=product_name, description=desc, price=price, image=image
        )

    return "Data successfully inputted"
