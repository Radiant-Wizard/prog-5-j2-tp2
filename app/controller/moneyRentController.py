from fastapi import APIRouter
from app.managers.moneyRentManager import MoneyRentManager


class MoneyRentController:
    def __init__(self, manager: MoneyRentManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/money-rents")
        def postRentMoney(data: dict):
            return {
                "id": self.manager.rentMoney(
                    data.get("amount"), data.get("interest"), data.get("renterId")
                )
            }

        @self.router.get("/money-rents")
        def getMoneyRents():
            return self.manager.listMoneyRents()
