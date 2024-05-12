from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=(255))
    guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self): 
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=(255))
    price = models.IntegerField()
    inventory = models.IntegerField()

    def __str__(self): 
        return self.title