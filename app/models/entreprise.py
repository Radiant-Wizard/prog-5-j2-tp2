from typing import override
from app.models.interfaces.rentableObject import RentableObject
from app.models.customer import Customer


class Entreprise(Customer):
    def __init__(self, name: str, currentRentals: list[RentableObject]):
        super().__init__(name, currentRentals)
        self.type = "ENTREPRISE"

    @override
    def getCurrentRentals(self):
        return self.currentRentals
