from app.managers.carRentController import CarRentManager


class CarRentController:
    def __init__(self, manager: CarRentManager):
        self.manager = manager

    def postRentCar(self, rentDurationInDay: int, carId: int, renterId: int):
        return self.manager.rentCar(rentDurationInDay, carId, renterId)

    def getCarRents(self):
        return self.manager.listCarRents()
