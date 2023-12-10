from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

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
    def bind_place(self, data: Dict[str, str | int], user_id: int, duration: int):
        try:
            parking_space = ParkingSpace.objects.filter(**data)[0]
        except (ValidationError, ValueError, IndexError):
            return None
        if parking_space:
            parking_space.status = True
            parking_space.user_id = user_id
            parking_space.duration = duration
            parking_space.save()
        else:
            return None
        return parking_space

    def update(self, data: Dict[str, str | int], user_id: int, status: int, duration: int):
        try:
            parking_space = ParkingSpace.objects.filter(**data)[0]
        except (ValidationError, IndexError):
            return None
        if parking_space:
            ParkingSpace.objects.filter(**data).update(
                user_id=user_id,
                status=status,
                duration=duration)
        return parking_space.id

    def delete(self, user_id, id):
        ParkingSpace.objects.filter(user_id=user_id, id=id).update(status=False, user_id=None, duration=None)


class ParkingSpaceDAL:
    def create(self, data: Dict[str, str | int]):
        try:
            parking_space = ParkingSpace.objects.create(**data)
        except (ValidationError, IntegrityError):
            return None
        parking_space.save()
        return parking_space

    def update(self, data: Dict[str, str | int], id: int):
        try:
            parking_space = ParkingSpace.objects.filter(id=id).update(
                date=data['date'],
                time=data['time'],
                location=data['location'])
        except (ValidationError, IntegrityError):
            return None
        return parking_space

    def delete(self, id):
        ParkingSpace.objects.filter(id=id).delete()
