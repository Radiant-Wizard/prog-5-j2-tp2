from app.managers.carManager import CarManager


class CarController:
    def __init__(self, manager: CarManager):
        self.manager = manager

    def postCar(self, dailyPrice: float):
        return self.manager.addCar(dailyPrice)

    def getCars(self):
        return self.manager.listCars()
