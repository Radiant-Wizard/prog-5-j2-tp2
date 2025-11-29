from psycopg2 import Error
from app.repository.moneyRentRepository import MoneyRentRepository


class MoneyRentService:
    def __init__(self, repository: MoneyRentRepository):
        self.repository = repository

    def rentMoney(self, renterId: int, amount: float, interest: float):
        try:
            return self.repository.create(
                renterId=renterId, amount=amount, interest=interest
            )
        except Error as e:
            raise RuntimeError("Failed to rent money") from e

    def getAllMoneyRents(self):
        try:
            return self.repository.getAll()
        except Error as e:
            raise RuntimeError("Failed to fetch money rents") from e
