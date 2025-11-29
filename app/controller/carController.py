from fastapi import APIRouter, HTTPException
from app.managers.carManager import CarManager


class CarController:
    def __init__(self, manager: CarManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/cars")
        def postCar(data: dict):
            try:
                return {
                    "id": self.manager.addCar(
                        str(data.get("carReference")),
                        data.get("dailyPrice"),  # type: ignore
                    )
                }
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")

        @self.router.get("/cars")
        def getCars():
            try:
                return self.manager.listCars()
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")
