from psycopg2 import Error
from app.repository.carRentRepository import CarRentRepository


class CarRentService:
    def __init__(self, repository: CarRentRepository):
        self.repository = repository

    def rentCar(self, renterId: int, carId: int, durationInDay: int):
        try:
            return self.repository.create(renterId, carId, durationInDay)
        except Error as e:
            raise RuntimeError("Failed to rent car") from e

    def getAllCarRents(self):
        try:
            return self.repository.getAll()
        except Error as e:
            raise RuntimeError("Failed to fetch car rents") from e
