from typing import override
from app.models.interfaces.rentableObject import RentableObject
from app.models.interfaces.renter import Renter


class Customer(Renter):
    def __init__(self, name: str, currentRentals: list[RentableObject]):
        self.name = name
        self.currentRentals = currentRentals
        self.type = ""

    @override
    def getTotalSpent(self):
        totalSpent = sum(renting.getRentalPrice() for renting in self.currentRentals)
        return totalSpent

    @override
    def rentObject(self, objectToRent):
        if objectToRent is not None:
            self.currentRentals.append(objectToRent)
            return True
        return False
