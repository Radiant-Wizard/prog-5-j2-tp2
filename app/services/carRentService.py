from app.repository.carRentRepository import CarRentRepository
from typing import List


class CarRentService:
    def __init__(self, repository: CarRentRepository):
        self.repository = repository

    def rentCar(self, rentDurationInDay: int, carId: int, renterId: int) -> int:
        return self.repository.create(rentDurationInDay, carId, renterId)

    def getAllCarRents(self) -> List[dict]:
        return self.repository.getAll()
