from django.db import models
from django.contrib.auth.models import User


class ParkingSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=255)
    time = models.TimeField()
    location = models.CharField(max_length=255)
    duration = models.IntegerField(null=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'ParkingSpace'
        unique_together = ('date', 'time', 'location')
