from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

class Volunteer(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Campaign_id = models.CharField(max_length=155)
    Email = models.EmailField(max_length=254)
    PhoneNumber = models.IntegerField()
    Country = models.CharField(max_length =120)
    State = models.CharField(max_length =120)
    City = models.CharField(max_length =120)

    def __str__(self):
        return self.Name
