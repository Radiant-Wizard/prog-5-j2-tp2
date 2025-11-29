from typing import List


class CarRentRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, rentDurationInDay: int, carId: int, renterId: int) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                        INSERT INTO 
                        carRent (rentDurationInDay, carId, renterId) 
                        VALUES (%s, %s, %s) RETURNING id
                        """,
                (rentDurationInDay, carId, renterId),
            )
            rentId = cur.fetchone()[0]
            self.conn.commit()
            return rentId

    def getAll(self) -> List[dict]:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, rentDurationInDay, carId, renterId FROM carRent")
            rows = cur.fetchall()
            return [
                {
                    "id": row[0],
                    "rentDurationInDay": row[1],
                    "carId": row[2],
                    "renterId": row[3],
                }
                for row in rows
            ]
