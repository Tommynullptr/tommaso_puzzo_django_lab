from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class User(models.Model):

    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    #should own a cart
    #wishlist?
    #cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)


class Cart(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)


class Wishlist(models.Model):

    listofproducts = models.ManyToManyField(Product)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    
