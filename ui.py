from session import Session
from controllers import AuthorizationController, UserController, ReservationController, ParkingSpaceController
from models import User


class UserInterface(Session):
    def __init__(self) -> None:
        self.__user: User = User()
        self.__user_controller: UserController = UserController()
        self.__reservation_controller: ReservationController = ReservationController()

    def start_session(self):
        pass

    def end_session(self):
        pass


class AdminInterace(Session):
    def __init__(self) -> None:
        self.__user: User = User()
        self.__user_controller: UserController = UserController()
        self.__parking_space_controller: ParkingSpaceController = ParkingSpaceController()

    def start_session(self):
        pass

    def end_session(self):
        pass


class AutorizationInterface(Session):
    def __init__(self) -> None:
        self.__authorization_controller: AuthorizationController = AuthorizationController()

    def start_session(self):
        pass

    def end_session(self):
        pass
