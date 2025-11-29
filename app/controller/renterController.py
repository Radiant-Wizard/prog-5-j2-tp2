from fastapi import APIRouter, HTTPException
from app.managers.renterManager import RenterManager


class RenterController:
    def __init__(self, manager: RenterManager):
        self.manager = manager
        self.router = APIRouter()

        @self.router.post("/renters")
        def postRenter(data: dict):
            try:
                return {
                    "id": self.manager.addRenter(
                        str(data.get("name")), str(data.get("renterType"))
                    )
                }
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")

        @self.router.get("/renters")
        def getRenters():
            try:
                return self.manager.listRenters()
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")
