from models import ParkingSpace, User


class UserDal:
    def __init__(self) -> None:
        self.db_session = ''

    def get(user_id: int) -> User:
        pass

    def save(user: User) -> None:
        pass

    def patch(user: User) -> None:
        pass

    def delete(user_ud: int) -> None:
        pass


class ParkingSpaceDAL:
    def __init__(self) -> None:
        self.db_session = ''

    def add(parking_space: ParkingSpace) -> None:
        pass

    def change(parking_space_id: int) -> None:
        pass


class ReservationDAL:
    def __init__(self) -> None:
        self.db_session = ''

    def add(parking_space: ParkingSpace) -> None:
        pass

    def delete(parking_space_id: int) -> None:
        pass

    def change(old_parking_space_id: int, new_parking_space: ParkingSpace) -> None:
        pass
