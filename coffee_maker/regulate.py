from abc import ABC, abstractmethod
import time


class Thermometer(ABC):
    @abstractmethod
    def read(self) -> float:
        pass


class Heater(ABC):
    @abstractmethod
    def engage(self):
        pass

    @abstractmethod
    def disengage(self):
        pass


def regulate(t: Thermometer, h: Heater, min_temp: float, max_temp: float):
    while True:
        while t.read() > min_temp:
            time.sleep(1)

        h.engage()  # 升温

        while t.read() < max_temp:
            time.sleep(1)

        h.disengage()  # 降温
