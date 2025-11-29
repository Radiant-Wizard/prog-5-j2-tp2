from app.services.moneyRentManager import MoneyRentService
from typing import List


class MoneyRentManager:
    def __init__(self, service: MoneyRentService):
        self.service = service

    def rentMoney(self, amount: float, interest: float, renterId: int) -> int:
        return self.service.rentMoney(amount, interest, renterId)

    def listMoneyRents(self) -> List[dict]:
        return self.service.getAllMoneyRents()
