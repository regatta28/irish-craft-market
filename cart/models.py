from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return "{0}".format(self.product.name)
