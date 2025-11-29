from psycopg2 import Error
from app.repository.carRepository import CarRepository
from app.models.car import Car


class CarService:
    def __init__(self, repository: CarRepository):
        self.repository = repository

    def createCar(self, car: Car):
        try:
            return self.repository.create(car)
        except Error as e:
            raise RuntimeError("Failed to create car") from e

    def getAllCars(self):
        try:
            return self.repository.getAll()
        except Error as e:
            raise RuntimeError("Failed to fetch cars") from e
