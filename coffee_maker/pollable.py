from abc import ABC, abstractmethod


class Pollable(ABC):
    @abstractmethod
    def poll(self):
        pass
