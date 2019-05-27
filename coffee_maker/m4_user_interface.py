from coffee_maker_api import CoffeeMakerAPI, BrewButtonStatus, IndicatorState
from user_interface import UserInterface
from pollable import Pollable


class M4UserInterface(UserInterface, Pollable):
    api: CoffeeMakerAPI

    def __init__(self, api: CoffeeMakerAPI):
        self.api = api
        super()

    def poll(self) -> None:
        status = self.api.get_brew_button_status()

        if status == BrewButtonStatus.PUSHED:
            self.start_brewing()

    def done(self):
        self.api.set_indicator_state(IndicatorState.ON)

    def complete_cycle(self):
        self.api.set_indicator_state(IndicatorState.OFF)
