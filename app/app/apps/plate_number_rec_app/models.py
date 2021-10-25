from django.db import models


class CarPlateNumber(models.Model):
    name = models.CharField(max_length=50)
    car_img = models.ImageField(upload_to='images/')
    detected_plate_img = models.ImageField(upload_to='images/')
    detected_each_char = models.ImageField(upload_to='images/')
    contour = models.ImageField(upload_to='images/')

    objects = models.Manager()