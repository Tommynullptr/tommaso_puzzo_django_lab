from django.db import models

# Create your models here.


class Product(models.Model):

    id = models.IntegerField(primary_key=True, unique=True,)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class User(models.Model):

    username = models.CharField(max_length=255, primary_key=True, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    #should own a cart
    #cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)


class Cart(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)


class Order(models.Model):

    listofproducts = models.ManyToManyField(Product)
    totalprice = models.FloatField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)


#TODO: alternative to manytomanyfield: add a field to the product model that is a list of users who have it in their cart and use a queryset
    
