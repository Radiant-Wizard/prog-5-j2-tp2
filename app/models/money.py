from typing import override
from app.models.interfaces.rentableObject import RentableObject


class Money(RentableObject):
    def __init__(self, amount: float, interest: float):
        self.amount = amount
        self.interest = interest

    @override
    def getRentalPrice(self):
        amountWithInterest = self.amount + self.interest
        return amountWithInterest
