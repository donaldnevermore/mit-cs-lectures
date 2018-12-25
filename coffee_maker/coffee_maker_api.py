from enum import Enum
from abc import ABC, abstractmethod


class WarmerPlateStatus(Enum):
    WARMER_EMPTY = 1
    POT_EMPTY = 2
    POT_NOT_EMPTY = 3


class BoilerStatus(Enum):
    EMPTY = 1
    NOT_EMPTY = 2


class BrewButtonStatus(Enum):
    PUSHED = 1
    NOT_PUSHED = 2


class BoilerState(Enum):
    ON = 1
    OFF = 2


class WarmerState(Enum):
    ON = 1
    OFF = 2


class IndicatorState(Enum):
    ON = 1
    OFF = 2


class ReliefValveState(Enum):
    OPEN = 1
    CLOSED = 2


class CoffeeMakerAPI(ABC):
    @abstractmethod
    def get_warmer_plate_status(self) -> WarmerPlateStatus:
        pass

    @abstractmethod
    def get_boiler_status(self) -> BoilerStatus:
        pass

    @abstractmethod
    def get_brew_button_status(self) -> BrewButtonStatus:
        pass

    @abstractmethod
    def set_boiler_state(self, s: BoilerState):
        pass

    @abstractmethod
    def set_warmer_state(self, s: WarmerState):
        pass

    @abstractmethod
    def set_indicator_state(self, s: IndicatorState):
        pass

    @abstractmethod
    def set_relief_valve_state(self, s: ReliefValveState):
        pass
