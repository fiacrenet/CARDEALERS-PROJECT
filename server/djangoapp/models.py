# Uncomment the following imports before adding the Model code

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    countryorigin = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make=models.ForeignKey(CarMake,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    CAR_TYPES=[
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CROSSOVER', 'Crossover'),
        ('HATCHBACK', 'Hatchback'),
        ]
    type=models.CharField(max_length=15,choices=CAR_TYPES,default='SUV')
    year=models.IntegerField(default=2024,
    validators=[
      MaxValueValidator(2024),
      MinValueValidator(2015)
             ])
 
    def __str__(self):
        return self.name