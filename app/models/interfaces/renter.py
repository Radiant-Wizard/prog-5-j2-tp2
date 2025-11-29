from abc import ABC, abstractmethod
from app.models.interfaces.rentableObject import RentableObject


class Renter(ABC):
    @abstractmethod
    def getCurrentRentals(self) -> list[RentableObject]:
        pass

    @abstractmethod
    def getTotalSpent(self) -> float:
        pass

    @abstractmethod
    def rentObject(self, objectToRent: RentableObject) -> bool:
        pass
