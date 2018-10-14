from coffee_maker_api import CoffeeMakerAPI, BoilerStatus, ReliefValueState, BoilerState


class M4HotWaterSource(HotWaterSource):
    api: CoffeeMakerAPI

    def __init__(self, api: CoffeeMakerAPI):
        self.api = api

    def is_ready(self) -> bool:
        status: BoilerStatus = self.api.get_boiler_status()

        return status == BoilerStatus.NOT_EMPTY

    def start(self) -> None:
        self.api.set_relief_value_state(ReliefValueState.CLOSED)
        self.api.set_boiler_state(BoilerState.ON)
