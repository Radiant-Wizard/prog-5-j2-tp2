from app.services.renterService import RenterService
from app.models.customer import Customer
from app.models.entreprise import Entreprise
from app.models.person import Person
from typing import List


class RenterManager:
    def __init__(self, service: RenterService):
        self.service = service

    def addRenter(self, name: str, type_: str) -> int:
        if str(type_) == "ENTREPRISE":
            renter = Entreprise(name, [])
            renter.type = type_
        renter = Person(name, [])
        renter.type = type_
        return self.service.createRenter(renter)

    def listRenters(self) -> List[Customer]:
        return self.service.getAllRenters()
