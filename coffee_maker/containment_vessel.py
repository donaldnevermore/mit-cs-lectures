from abc import ABC, abstractmethod
from typing import Any


class ContainmentVessel(ABC):
    ui: Any
    hws: Any
    is_brewing: bool = False
    is_complete: bool = True

    def init(self, ui, hws):
        self.ui = ui
        self.hws = hws

    def start(self):
        self.is_brewing = True
        self.is_complete = False

    def done(self):
        self.is_brewing = False

    def declare_complete(self):
        self.is_complete = True
        self.ui.complete()

    def container_available(self):
        self.hws.resume()

    def container_unavailable(self):
        self.hws.pause()

    @abstractmethod
    def is_ready(self) -> bool:
        pass
