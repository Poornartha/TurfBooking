from django.db import models
from datetime import date
from django.utils import timezone


# Create your models here.


class Turf(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bookie(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name


class Slot(models.Model):
    turf = models.ForeignKey(Turf, default=1, on_delete=models.SET_DEFAULT)
    timing = models.TimeField(default=timezone.now())
    user = models.ForeignKey(Bookie, default=1, on_delete=models.SET_DEFAULT)
    book_timing = models.DateTimeField(auto_now_add=True)
