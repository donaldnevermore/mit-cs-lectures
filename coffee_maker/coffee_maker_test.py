from .coffee_maker_api import *
from .m4_user_interface import M4UserInterface
from .m4_hot_water_source import M4HotWaterSource
from .m4_containment_vessel import M4ContainmentVessel


class CoffeeMakerStub(CoffeeMakerAPI):
    button_pressed: bool = False
    light_on: bool = False
    boiler_on: bool = False
    valve_closed: bool = True
    plate_on: bool = False
    boiler_empty: bool = True
    pot_present: bool = True
    pot_not_empty: bool = False

    def get_warmer_plate_status(self) -> WarmerPlateStatus:
        if not self.pot_present:
            return WarmerPlateStatus.WARMER_EMPTY
        elif self.pot_not_empty:
            return WarmerPlateStatus.POT_EMPTY

    def get_boiler_status(self) -> BoilerStatus:
        return BoilerStatus.EMPTY if self.boiler_empty else BoilerStatus.NOT_EMPTY

    def get_brew_button_status(self) -> BrewButtonStatus:
        if self.button_pressed:
            self.button_pressed = False
            return BrewButtonStatus.PUSHED
        else:
            return BrewButtonStatus.NOT_PUSHED

    def set_boiler_state(self, boiler_state: BoilerState):
        self.boiler_on = boiler_state == BoilerState.ON

    def set_warmer_state(self, warmer_state: WarmerState):
        self.plate_on = warmer_state == WarmerState.ON

    def set_indicator_state(self, indicator_state: IndicatorState):
        self.light_on = indicator_state == IndicatorState.ON

    def set_relief_valve_state(self, relief_valve_state: ReliefValveState):
        self.valve_closed = relief_valve_state == ReliefValveState.CLOSED


def set_up():
    api = CoffeeMakerStub()
    ui = M4UserInterface(api)
    hws = M4HotWaterSource(api)
    cv = M4ContainmentVessel(api)

    ui.init(hws, cv)
    hws.init(ui, cv)
    cv.init(ui, hws)

    ui.poll()
    hws.poll()
    cv.poll()

    return api, ui, hws, cv


def test_initial_conditions():
    api, ui, hws, cv = set_up()
    assert api.boiler_on == False
    assert api.light_on == False
    assert api.plate_on == False
    assert api.valve_closed == True
