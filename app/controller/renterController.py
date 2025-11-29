from fastapi import APIRouter
from app.managers.renterManager import RenterManager


class RenterController:
    def __init__(self, manager: RenterManager):
        self.manager = manager
        self.router = APIRouter()

        # Define endpoints directly
        @self.router.post("/renters")
        def postRenter(data: dict):
            return {"id": self.manager.addRenter(data.get("name"), data.get("type_"))}

        @self.router.get("/renters")
        def getRenters():
            return self.manager.listRenters()
