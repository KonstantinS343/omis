from django.db import models


class ParkingSpace(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    status = models.BooleanField()

    class Meta:
        db_table = 'ParkingSpace'
