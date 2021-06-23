from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)


class Pizza(models.Model):
    name = models.CharField(max_length=128)
    cheese = models.CharField(max_length=128)
    pastry = models.CharField(max_length=128)
    secret_ingredient = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)