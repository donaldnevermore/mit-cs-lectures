from abc import ABC, abstractmethod
from typing import Any


class HotWaterSource(ABC):
    ui: Any
    cv: Any
    is_brewing: bool = False

    def init(self, ui, cv):
        self.ui = ui
        self.cv = cv

    def start(self):
        self.is_brewing = True
        self.start_brewing()

    def done(self):
        self.is_brewing = False

    def declare_done(self):
        self.ui.done()
        self.cv.done()
        self.is_brewing = False

    @abstractmethod
    def is_ready(self) -> bool:
        pass

    @abstractmethod
    def start_brewing(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass
