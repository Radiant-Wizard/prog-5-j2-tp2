from typing import List
from app.models.customer import Customer
from app.models.entreprise import Entreprise
from app.models.person import Person


class RenterRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, renter: Customer) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    INSERT INTO renter (name, type)
                    VALUES (%s, %s) 
                    RETURNING id
                    """,
                (renter.name, renter.type),
            )
            renterId = cur.fetchone()[0]
            self.conn.commit()
            return renterId

    def getAll(self) -> List[Customer]:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, name, type FROM renter")
            rows = cur.fetchall()
            result = []
            for row in rows:
                if str(row[2]) == "ENTREPRISE":
                    renter = Entreprise(row[1], [])
                    renter.type = row[2]
                renter = Person(row[1], [])
                result.append(renter)

            return result
