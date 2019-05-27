from coffee_maker_api import CoffeeMakerAPI, WarmerPlateStatus, WarmerState
from containment_vessel import ContainmentVessel
from pollable import Pollable


class M4ContainmentVessel(ContainmentVessel, Pollable):
    api: CoffeeMakerAPI
    last_pot_status: WarmerPlateStatus

    def __init__(self, api: CoffeeMakerAPI):
        self.api = api
        self.last_pot_status = WarmerPlateStatus.POT_EMPTY
        super()

    def is_ready(self) -> bool:
        status: WarmerPlateStatus = self.api.get_warmer_plate_status()

        return status == WarmerPlateStatus.POT_EMPTY

    def poll(self) -> None:
        pot_status = self.api.get_warmer_plate_status()

        if pot_status != self.last_pot_status:
            if self.is_brewing:
                self.handle_brewing_event(pot_status)
            elif not self.is_complete:
                self.handle_incomplete_event(pot_status)

            self.last_pot_status = pot_status

    def handle_brewing_event(self, pot_status):
        if pot_status == WarmerPlateStatus.POT_NOT_EMPTY:
            self.container_available()
            self.api.set_warmer_state(WarmerState.ON)
        elif pot_status == WarmerPlateStatus.WARMER_EMPTY:
            self.container_unavailable()
            self.api.set_warmer_state(WarmerState.OFF)
        else:
            # pot_status == POT_EMPTY
            self.container_available()
            self.api.set_warmer_state(WarmerState.OFF)

    def handle_incomplete_event(self, pot_status):
        if pot_status == WarmerPlateStatus.POT_NOT_EMPTY:
            self.api.set_warmer_state(WarmerState.ON)
        elif pot_status == WarmerPlateStatus.WARMER_EMPTY:
            self.api.set_warmer_state(WarmerState.OFF)
        else:
            self.api.set_warmer_state(WarmerState.OFF)
            self.declare_complete()
