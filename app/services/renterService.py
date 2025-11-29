from psycopg2 import Error
from app.repository.renterRepository import RenterRepository
from app.models.customer import Customer


class RenterService:
    def __init__(self, repository: RenterRepository):
        self.repository = repository

    def createRenter(self, renter: Customer) -> int:
        try:
            return self.repository.create(renter)
        except Error as e:
            raise RuntimeError("Failed to create renter") from e

    def getAllRenters(self):
        try:
            return self.repository.getAll()
        except Error as e:
            raise RuntimeError("Failed to fetch renters") from e
