from typing import List
from app.services.moneyRentService import MoneyRentService


class MoneyRentManager:
    def __init__(self, service: MoneyRentService):
        self.service = service

    def rentMoney(self, renterId: int, amount: float, interest: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if interest < 0:
            raise ValueError("Interest cannot be negative")

        return self.service.rentMoney(
            renterId=renterId, amount=amount, interest=interest
        )

    def listMoneyRents(self) -> List[dict]:
        return self.service.getAllMoneyRents()
