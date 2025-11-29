from fastapi import APIRouter, HTTPException
from app.managers.moneyRentManager import MoneyRentManager


class MoneyRentController:
    def __init__(self, manager: MoneyRentManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/money-rents")
        def postMoneyRent(data: dict):
            try:
                return {
                    "id": self.manager.rentMoney(
                        data.get("renterId"), data.get("amount"), data.get("interest")
                    )
                }
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")

        @self.router.get("/money-rents")
        def getMoneyRents():
            try:
                return self.manager.listMoneyRents()
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")
