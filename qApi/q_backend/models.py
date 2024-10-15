from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    logo_link = models.CharField(max_length=255, null=False, blank=False)
    x_enter = models.IntegerField()
    y_enter = models.IntegerField()
    x_exit = models.IntegerField()
    y_exit = models.IntegerField()
    address = models.CharField(max_length=255, null=False, blank=False)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    category = models.CharField(max_length=255, null=False, blank=False)
    image_link = models.CharField(max_length=500, null=False, blank=False, unique=True)


class ShopProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField(default=0.0)
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
