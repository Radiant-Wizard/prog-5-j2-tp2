from app.models.car import Car
from typing import List


class CarRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, car: Car) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO car (carReference, dailyPrice) VALUES (%s, %s) RETURNING id",
                (f"CAR{car.dailyPrice:.0f}", car.dailyPrice),
            )
            carId = cur.fetchone()[0]
            self.conn.commit()
            return carId

    def getAll(self) -> List[Car]:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, dailyPrice FROM car")
            rows = cur.fetchall()
            result = []
            for row in rows:
                result.append(Car(row[1], 0))
            return result

