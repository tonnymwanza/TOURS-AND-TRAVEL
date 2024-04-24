from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

class Booking(models.Model):
    destination = models.CharField(max_length=30)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()


    
class Trending(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=40)
    image = models.ImageField()


class Rooms(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=255)
    hotel_name = models.CharField(max_length=100)