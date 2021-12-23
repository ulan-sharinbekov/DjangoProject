from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=200)
    year = models.IntegerField(default=1990)
    color = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    engine = models.FloatField()

    def __str__(self):
        return f'{self.brand, self.color, self.engine, self.year, self.type}'


class Brand(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name, self.country}'

class Vehicle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    year = models.IntegerField(default=1990)
    color = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="get_vehicles")

    def __str__(self):
        return f'{self.title, self.year}'