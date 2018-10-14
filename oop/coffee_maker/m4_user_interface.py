from coffee_maker_api import *
from user_interface import UserInterface


class M4UserInterface(UserInterface):
    def check_button(self) -> None:
        status = CoffeeMaker.api.get_brew_button_status()

        if status == BrewButtonStatus.PUSHED:
            start_brewing()
