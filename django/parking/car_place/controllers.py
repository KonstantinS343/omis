from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError

from functools import reduce

from .manager import UserDAL, ReservationDAL, ParkingSpaceDAL


class AuthorizationController:
    def __init__(self) -> None:
        self.__user_dal = UserDAL()

    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            return None, "Username or password cannot be empty."

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return user.id, "Good"
        return None, "Invalid username or password."

    def register(self, request):
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not username or not password:
            return None, "Username or password cannot be empty."
        if password != password2:
            return None, "Passwords must match."
        try:
            self.__user_dal.create(username=username, password=password)
        except IntegrityError:
            return None, "Such user already exist."
        return username, "Good"


class ReservationController:
    def __init__(self) -> None:
        self.__reservation_dal: ReservationDAL = ReservationDAL()

    def add_reservation(self, request) -> None:
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        data = {key: reduce(lambda x, y: x + y, value) for key, value in data.items()}
        try:
            int(data['duration'])
        except Exception:
            return None, "Check the entered data"
        duration = int(data.pop('duration'))
        data['status'] = 0
        result = self.__reservation_dal.bind_place(data, request.user.id, duration)
        if not result:
            return None, "Check the entered data"
        return request.user.id, "Good"

    def delete_reservation(self, user_id, id) -> None:
        self.__reservation_dal.delete(user_id=user_id, id=id)

    def change_reservation(self, request) -> None:
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        data = {key: reduce(lambda x, y: x + y, value) for key, value in data.items()}
        try:
            int(data['duration'])
        except Exception:
            return None, "Check the entered data"
        result = self.__reservation_dal.update(data=data, user_id=request.user.id, status=1,
                                               duration=data.pop('duration'))
        if not result:
            return None, "Check the entered data"
        if result != int(request.path.split('/')[-2]):
            self.delete_reservation(user_id=request.user.id, id=request.path.split('/')[-2])
        return request.user.id, "Good"


class ParkingSpaceController:
    def __init__(self) -> None:
        self.__parking_space_dal: ParkingSpaceDAL = ParkingSpaceDAL()

    def add_parking_space(self, request) -> None:
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        data = {key: reduce(lambda x, y: x + y, value) for key, value in data.items()}
        result = self.__parking_space_dal.create(data)
        if not result:
            return None, "Check the entered data"
        return request.user.id, "Good"

    def delete_parking_space(self, id) -> None:
        self.__parking_space_dal.delete(id=id)

    def change_parking_space(self, request, id) -> None:
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        data = {key: reduce(lambda x, y: x + y, value) for key, value in data.items()}
        result = self.__parking_space_dal.update(data, id)
        if not result:
            return None, "Check the entered data"
        return request.user.id, "Good"
