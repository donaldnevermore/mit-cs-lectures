from coffee_maker_api import CoffeeMakerAPI, WarmerPlateStatus


class M4ContainmentVessel(ContainmentVessel):
    api: CoffeeMakerAPI
    is_brewing: bool = False

    def __init__(self, api: CoffeeMakerAPI):
        self.api = api

    def is_ready(self) -> bool:
        status: WarmerPlateStatus = self.api.get_warmer_plate_status()

        return status == WarmerPlateStatus.POT_EMPTY

    def start(self) -> None:
        self.is_brewing = True
