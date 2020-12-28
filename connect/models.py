from django.db import models


# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_model_name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.car_model_name


class Car(models.Model):
    car_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, blank=True, null=True)
    car_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.car_name
