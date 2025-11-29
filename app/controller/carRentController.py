from fastapi import APIRouter
from app.managers.carRentManager import CarRentManager


class CarRentController:
    def __init__(self, manager: CarRentManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/car-rents")
        def postRentCar(data: dict):
            """Expects {"rentDurationInDay": 5, "carId": 1, "renterId": 2}"""
            return {
                "id": self.manager.rentCar(
                    data.get("rentDurationInDay"),
                    data.get("carId"),
                    data.get("renterId"),
                )
            }

        @self.router.get("/car-rents")
        def getCarRents():
            return self.manager.listCarRents()
