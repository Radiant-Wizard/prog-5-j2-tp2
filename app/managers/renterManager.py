from app.services.renterService import RenterService
from app.models.customer import Customer
from typing import List


class RenterManager:
    def __init__(self, service: RenterService):
        self.service = service

    def addRenter(self, name: str, type_: str) -> int:
        renter = Customer(name, [])
        renter.type = type_
        return self.service.createRenter(renter)

    def listRenters(self) -> List[Customer]:
        return self.service.getAllRenters()
