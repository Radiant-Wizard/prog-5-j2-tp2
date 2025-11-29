from typing import List
from app.services.carRentService import CarRentService


class CarRentManager:
    def __init__(self, service: CarRentService):
        self.service = service

    def rentCar(self, renterId: int, carId: int, durationInDay: int):
        if durationInDay <= 0:
            raise ValueError("Duration must be positive")

        return self.service.rentCar(renterId, carId, durationInDay)

    def listCarRents(self) -> List[dict]:
        return self.service.getAllCarRents()
