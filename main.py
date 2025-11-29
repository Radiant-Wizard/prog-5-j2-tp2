from fastapi import FastAPI
from app.database.connection import getConnection
from app.repository.renterRepository import RenterRepository
from app.repository.carRepository import CarRepository
from app.repository.carRentRepository import CarRentRepository
from app.repository.moneyRentRepository import MoneyRentRepository

from app.services.renterService import RenterService
from app.services.carService import CarService
from app.services.carRentService import CarRentService
from app.services.moneyRentService import MoneyRentService

from app.managers.renterManager import RenterManager
from app.managers.carManager import CarManager
from app.managers.carRentManager import CarRentManager
from app.managers.moneyRentManager import MoneyRentManager

from app.controllers.renterController import RenterController
from app.controllers.carController import CarController
from app.controllers.carRentController import CarRentController
from app.controllers.moneyRentController import MoneyRentController

app = FastAPI(title="Renting API")

conn = getConnection()

renterController = RenterController(
    RenterManager(RenterService(RenterRepository(conn)))
)
carController = CarController(CarManager(CarService(CarRepository(conn))))
carRentController = CarRentController(
    CarRentManager(CarRentService(CarRentRepository(conn)))
)
moneyRentController = MoneyRentController(
    MoneyRentManager(MoneyRentService(MoneyRentRepository(conn)))
)

app.include_router(renterController.router)
app.include_router(carController.router)
app.include_router(carRentController.router)
app.include_router(moneyRentController.router)
