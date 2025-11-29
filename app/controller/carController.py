from fastapi import APIRouter
from app.managers.carManager import CarManager


class CarController:
    def __init__(self, manager: CarManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/cars")
        def postcar(data: dict):
            return {"id": self.manager.addCar(data.get("dailyPrice"))}

        @self.router.get("/cars")
        def getcars():
            return self.manager.listcars()
