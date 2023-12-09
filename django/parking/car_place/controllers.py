from django.contrib.auth import authenticate, login

from functools import reduce

from .manager import UserDAL, ReservationDAL
from .models import ParkingSpace


class AuthorizationController:
    def __init__(self) -> None:
        self.user_dal = UserDAL()

    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return user.id
        return None

    def register(self, request):
        username = request.POST['username']
        password = request.POST['password']
        self.user_dal.create(username=username, password=password)
        return None


class ReservationController:
    def __init__(self) -> None:
        self.__reservation_dal: ReservationDAL = ReservationDAL()

    def add_reservation(self, request) -> None:
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        data = {key: reduce(lambda x, y: x + y, value) for key, value in data.items()}
        data['user_id'] = request.user.id
        places = ParkingSpace.objects.filter(location=data['location'])
        if places:
            return None
        self.__reservation_dal.add(data)

    def delete_reservation(self, id) -> None:
        self.__reservation_dal.delete(id=id)

    def change_reservation(self, request, id) -> None:
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        data = {key: reduce(lambda x, y: x + y, value) for key, value in data.items()}
        data['user_id'] = request.user.id
        places = ParkingSpace.objects.filter(location=data['location'])
        if places:
            return None
        self.__reservation_dal.update(data, id)


# class ParkingSpaceController:
#     def __init__(self) -> None:
#         self.__parking_space_dal: ParkingSpaceDAL = ParkingSpaceDAL()

#     def add_parking_space(amount: int, parking_space: ParkingSpace) -> None:
#         pass

#     def change_parking_space(parking_space: ParkingSpace) -> None:
#         pass
