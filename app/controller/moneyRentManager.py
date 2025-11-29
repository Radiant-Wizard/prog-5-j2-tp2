from app.managers.moneyRentManager import MoneyRentManager


class MoneyRentController:
    def __init__(self, manager: MoneyRentManager):
        self.manager = manager

    def postRentMoney(self, amount: float, interest: float, renterId: int):
        return self.manager.rentMoney(amount, interest, renterId)

    def getMoneyRents(self):
        return self.manager.listMoneyRents()
