from app.repository.carRepository import CarRepository
from app.models.car import Car
from typing import List


class CarService:
    def __init__(self, repository: CarRepository):
        self.repository = repository

    def createCar(self, car: Car) -> int:
        return self.repository.create(car)

    def getAllCars(self) -> List[Car]:
        return self.repository.getAll()
