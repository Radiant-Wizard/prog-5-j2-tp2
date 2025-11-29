from typing import List


class MoneyRentRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, amount: float, interest: float, renterId: int) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO moneyRent (amount, interest, renterId) VALUES (%s, %s, %s) RETURNING id",
                (amount, interest, renterId),
            )
            moneyRentId = cur.fetchone()[0]
            self.conn.commit()
            return moneyRentId

    def getAll(self) -> List[dict]:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, amount, interest, renterId FROM moneyRent")
            rows = cur.fetchall()
            return [
                {"id": row[0], "amount": row[1], "interest": row[2], "renterId": row[3]}
                for row in rows
            ]
