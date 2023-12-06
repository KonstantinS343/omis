from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .manager import UserDAL


class AuthorizationController:
    def __init__(self) -> None:
        self.user_dal = UserDAL()

    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return user.id
        return None

    def register(self, request):
        username = request.POST['username']
        password = request.POST['password']
        self.user_dal.create(username=username, password=password)
        return None


# class ReservationController:
#     def __init__(self) -> None:
#         self.__reservation_dal: ReservationDAL = ReservationDAL()
# 
#     def add_reservation(parking_space: ParkingSpace) -> None:
#         pass
# 
#     def delete_reservation(parking_space: ParkingSpace) -> None:
#         pass
# 
#     def change_reservation(old_parking_space: ParkingSpace, new_parking_space: ParkingSpace) -> None:
#         pass
# 
# 
# class ParkingSpaceController:
#     def __init__(self) -> None:
#         self.__parking_space_dal: ParkingSpaceDAL = ParkingSpaceDAL()
# 
#     def add_parking_space(amount: int, parking_space: ParkingSpace) -> None:
#         pass
# 
#     def change_parking_space(parking_space: ParkingSpace) -> None:
#         pass
