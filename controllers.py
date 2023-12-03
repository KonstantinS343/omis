from dals import ReservationDAL, UserDal, ParkingSpaceDAL
from models import ParkingSpace, User


class AuthorizationController:
    def __init__(self) -> None:
        self.username: str = ''
        self.email: str = ''
        self.phone_number: str = ''
        self.__password: str = ''

    def login():
        pass

    def register():
        pass


class ReservationController:
    def __init__(self) -> None:
        self.__reservation_dal: ReservationDAL = ReservationDAL()

    def add_reservation(parking_space: ParkingSpace) -> None:
        pass

    def delete_reservation(parking_space: ParkingSpace) -> None:
        pass

    def change_reservation(old_parking_space: ParkingSpace, new_parking_space: ParkingSpace) -> None:
        pass


class ParkingSpaceController:
    def __init__(self) -> None:
        self.__parking_space_dal: ParkingSpaceDAL = ParkingSpaceDAL()

    def add_parking_space(amount: int, parking_space: ParkingSpace) -> None:
        pass

    def change_parking_space(parking_space: ParkingSpace) -> None:
        pass


class UserController:
    def __init__(self) -> None:
        self.__user_dal: UserDal = UserDal()

    def get_user(user_id: int) -> User:
        pass

    def save_user(user: User) -> None:
        pass

    def patch_user(user: User) -> None:
        pass

    def delete_user(user_id: int) -> None:
        pass
