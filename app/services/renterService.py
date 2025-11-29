from app.repository.renterRepository import RenterRepository
from app.models.customer import Customer
from typing import List


class RenterService:
    def __init__(self, repository: RenterRepository):
        self.repository = repository

    def createRenter(self, renter: Customer) -> int:
        return self.repository.create(renter)

    def getAllRenters(self) -> List[Customer]:
        return self.repository.getAll()
