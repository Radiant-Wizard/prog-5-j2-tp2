from app.services.carSerice import CarService
from app.models.car import Car
from typing import List


class CarManager:
    def __init__(self, service: CarService):
        self.service = service

    def addCar(self, dailyPrice: float) -> int:
        car = Car(dailyPrice, 0)
        return self.service.createCar(car)

    def listCars(self) -> List[Car]:
        return self.service.getAllCars()
