
# Create your models here.
from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.ImageField(default='test.jpeg', null=True, upload_to='event/')
    def __str__(self):
        return self.shop_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.FloatField()
    old_price = models.IntegerField()
    def __str__(self):
        return self.product_name
    

class Deal(models.Model):
    deal_name = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_till = models.DateField()
    discount_percent = models.FloatField()
    done_by = models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.deal_name
