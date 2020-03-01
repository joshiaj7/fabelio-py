from django.db import models

# Create your models here.


class Product(models.Model):
    link_str = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name
