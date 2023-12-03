from typing import List
from datetime import date


class User:
    def __init__(self) -> None:
        self.username: str = ''
        self.email: str = ''
        self.phone_number: str = ''
        self.__password: str = ''


class DefaultUser(User):
    def __init__(self) -> None:
        self._role: str = 'DefaultUser'
        self.user_id: int = 0
        self.reservations_ids: List[int] = []


class Admin(User):
    def __init__(self) -> None:
        self._role: str = 'DefaultUser'
        self.user_id: int = 0


class ParkingSpace:
    def __init__(self) -> None:
        self.id: int = 0
        self.date: date = date()
        self.time: date = date()
        self.location: str = ''
        self.status: bool = True
