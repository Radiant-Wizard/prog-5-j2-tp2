from typing import override
from app.models.interfaces.rentableObject import RentableObject


class Car(RentableObject):
    def __init__(self, dailyPrice: float, durationInDay: int):
        self.durationInDay = durationInDay
        self.dailyPrice = dailyPrice
        self.carReference = ""

    @override
    def getRentalPrice(self):
        rentalPriceForDayCount = float(self.durationInDay) * self.dailyPrice
        return rentalPriceForDayCount
