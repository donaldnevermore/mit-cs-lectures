from coffee_maker_api import CoffeeMakerAPI, BoilerStatus, ReliefValveState, BoilerState
from hot_water_source import HotWaterSource


class M4HotWaterSource(HotWaterSource):
    api: CoffeeMakerAPI

    def __init__(self, api: CoffeeMakerAPI):
        self.api = api
        super()

    def is_ready(self) -> bool:
        status: BoilerStatus = self.api.get_boiler_status()

        return status == BoilerStatus.NOT_EMPTY

    def start_brewing(self) -> None:
        self.api.set_relief_valve_state(ReliefValveState.CLOSED)
        self.api.set_boiler_state(BoilerState.ON)

    def poll(self):
        boiler_status = self.api.get_boiler_status()

        if self.is_brewing:
            if boiler_status == BoilerStatus.EMPTY:
                self.api.set_boiler_state(BoilerState.OFF)
                self.api.set_relief_valve_state(ReliefValveState.CLOSED)
                self.declare_done()

    def pause(self):
        self.api.set_boiler_state(BoilerState.OFF)
        self.api.set_relief_valve_state(ReliefValveState.OPEN)

    def resume(self):
        self.api.set_boiler_state(BoilerState.ON)
        self.api.set_relief_valve_state(ReliefValveState.CLOSED)
