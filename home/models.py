from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

class Product(models.Model):
    name= models.CharField(max_length=50)
    price = models.IntegerField()
    seller_name = models.CharField()

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)