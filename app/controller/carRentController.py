from fastapi import APIRouter, HTTPException
from app.managers.carRentManager import CarRentManager


class CarRentController:
    def __init__(self, manager: CarRentManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/car-rents")
        def postCarRent(data: dict):
            try:
                return {
                    "id": self.manager.rentCar(
                        data.get("renterId"),
                        data.get("carId"),
                        data.get("durationInDay"),
                    )
                }

            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")

        @self.router.get("/car-rents")
        def getCarRents():
            try:
                return self.manager.listCarRents()
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")
