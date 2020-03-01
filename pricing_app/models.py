from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    link_str = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(default=0)
    image = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name
