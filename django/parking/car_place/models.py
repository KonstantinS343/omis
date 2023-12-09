from django.db import models
from django.contrib.auth.models import User


class ParkingSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=255)
    time = models.TimeField()
    location = models.CharField(max_length=255)
    duration = models.IntegerField()
    status = models.BooleanField()

    class Meta:
        db_table = 'ParkingSpace'
