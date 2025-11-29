from typing import List
from app.services.renterService import RenterService
from app.models.customer import Customer
from app.models.entreprise import Entreprise
from app.models.person import Person


class RenterManager:
    def __init__(self, service: RenterService):
        self.service = service

    def addRenter(self, name: str, renterType: str) -> int:
        if not name:
            raise ValueError("Name cannot be empty")

        if renterType not in ["PERSONAL", "ENTREPRISE"]:
            raise ValueError("Invalid renter type")

        renter = (
            Entreprise(name=name, currentRentals=[])
            if renterType == "ENTREPRISE"
            else Person(name=name, currentRentals=[])
        )

        return self.service.createRenter(renter)

    def listRenters(self) -> List[Customer]:
        return self.service.getAllRenters()
