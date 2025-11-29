from fastapi import APIRouter
from app.managers.carMenager import carManager


class carcontroller:
    def __init__(self, manager: carManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/cars")
        def postcar(data: dict):
            """expects {"dailyprice": 100.0}"""
            return {"id": self.manager.addCar(data.get("dailyPrice"))}

        @self.router.get("/cars")
        def getcars():
            return self.manager.listcars()
