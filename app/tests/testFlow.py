from app.database.connection import getConnection
from app.repository.renterRepository import RenterRepository
from app.models.person import Person
from app.models.entreprise import Entreprise


def test_renter_repository():
    conn = getConnection()
    repo = RenterRepository(conn)

    person = Person(name="Alice", currentRentals=[])
    person.type = "PERSONAL"
    person_id = repo.create(person)
    print(f"Created Person with ID: {person_id}")

    entreprise = Entreprise(name="Acme Corp", currentRentals=[])
    entreprise.type = "ENTREPRISE"
    entreprise_id = repo.create(entreprise)
    print(f"Created Entreprise with ID: {entreprise_id}")

    renters = repo.getAll()
    print("All renters:")
    for r in renters:
        print(f"- {r.name} ({r.type})")

    conn.rollback()
    conn.close()


if __name__ == "__main__":
    test_renter_repository()
