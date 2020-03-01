from django.test import TestCase
from .models import Product

# Create your tests here.
class BasicTest(TestCase):
    def test_field(self):
        product = Product()
        product.link_str = "https://fabelio.com/ip/jobi-armchair.html"
        product.name = "Sofa 1 Dudukan Jobi"
        product.description = "Kenangan bersama keluarga tidak hanya melibatkan orang-orang di dalamnya, melainkan juga semua elemen yang dibangun di sekitarnya termasuk perabot rumah. Setelah bertahun-tahun ada di dalam rumah, maka secara otomatis sebuah sofa pun juga ikut menjadi bagian dari kenangan itu sendiri."
        product.price = 2474250
        product.image = "https://m2fabelio.imgix.net/catalog/product/cache/image/e9c3970ab036de70892d86c6d221abfe/j/o/Jobi_Armchair_(Teal)_3.JPG"
        product.save()

        record = Product.objects.get(pk=1)
        self.assertEqual(record, product)
