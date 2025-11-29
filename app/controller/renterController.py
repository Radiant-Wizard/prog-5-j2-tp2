from app.managers.renterManager import RenterManager


class RenterController:
    def __init__(self, manager: RenterManager):
        self.manager = manager

    def postRenter(self, name: str, type_: str):
        return self.manager.addRenter(name, type_)

    def getRenters(self):
        return self.manager.listRenters()
