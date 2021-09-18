from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='product_images')
    price=models.FloatField()

    def __str__(self) -> str:
        return str(self.name)

#Register it in admin
from django.contrib import admin
admin.site.register(Product)
