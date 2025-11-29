from app.services.carRentService import CarRentService
from typing import List


class CarRentManager:
    def __init__(self, service: CarRentService):
        self.service = service

    def rentCar(self, rentDurationInDay: int, carId: int, renterId: int) -> int:
        return self.service.rentCar(rentDurationInDay, carId, renterId)

    def listCarRents(self) -> List[dict]:
        return self.service.getAllCarRents()
