from typing import List
from app.services.carService import CarService
from app.models.car import Car


class CarManager:
    def __init__(self, service: CarService):
        self.service = service

    def addCar(self, carReference: str, dailyPrice: float):
        if not carReference:
            raise ValueError("Car reference cannot be empty")

        if dailyPrice <= 0:
            raise ValueError("Daily price must be positive")

        car = Car(dailyPrice=dailyPrice, durationInDay=0)
        car.carReference = carReference

        return self.service.createCar(car)

    def listCars(self) -> List[Car]:
        return self.service.getAllCars()
