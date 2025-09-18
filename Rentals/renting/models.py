from django.db import models

# Table 1: Customers
class Customer(models.Model):
    name = models.CharField(max_length=100)   # Column: name
    email = models.EmailField(unique=True)    # Column: email
    phone = models.CharField(max_length=15)   # Column: phone

    def __str__(self):
        return self.name

# Table 2: Cars
class Car(models.Model):
    brand = models.CharField(max_length=50)   # Column: brand
    model = models.CharField(max_length=50)   # Column: model
    year = models.IntegerField()              # Column: year
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
