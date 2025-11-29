from typing import override
from app.models.customer import Customer
from app.models.interfaces.rentableObject import RentableObject


class Person(Customer):
    def __init__(self, name: str, currentRentals: list[RentableObject]):
        super().__init__(name, currentRentals)
        self.type = "PERSONAL"

    @override
    def getCurrentRentals(self):
        return self.currentRentals
