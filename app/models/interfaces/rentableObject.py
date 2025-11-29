from abc import ABC, abstractmethod


class RentableObject(ABC):
    @abstractmethod
    def getRentalPrice(self) -> float:
        pass
