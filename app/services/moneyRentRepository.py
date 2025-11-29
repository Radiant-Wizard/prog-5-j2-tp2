from app.repository.moneyRent import MoneyRentRepository
from typing import List


class MoneyRentService:
    def __init__(self, repository: MoneyRentRepository):
        self.repository = repository

    def rentMoney(self, amount: float, interest: float, renterId: int) -> int:
        return self.repository.create(amount, interest, renterId)

    def getAllMoneyRents(self) -> List[dict]:
        return self.repository.getAll()
