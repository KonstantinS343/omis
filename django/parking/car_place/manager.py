from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from typing import Dict

from .models import ParkingSpace


class UserDAL:
    def get(self, user_id: int):
        return User.objects.get(id=user_id)

    def create(self, username: str, password: str):
        user = User.objects.create_user(username=username, password=password)
        user.save()

    def delete(self, user_id):
        User.objects.delete(id=user_id)


class ReservationDAL:
    def add(self, data: Dict[str, str | int]):
        try:
            parking_space = ParkingSpace.objects.create(**data)
        except ValidationError:
            return None
        parking_space.save()

    def update(self, data: Dict[str, str | int], id: int):
        user_id = data.pop('user_id')
        try:
            ParkingSpace.objects.filter(user_id=user_id, id=id).update(
                date=data['date'],
                time=data['time'],
                location=data['location'],
                duration=data['duration'])
        except ValidationError:
            return None

    def delete(self, id):
        ParkingSpace.objects.filter(id=id).delete()
