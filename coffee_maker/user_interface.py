from abc import ABC, abstractmethod


class UserInterface(ABC):
    hws: any
    cv: any
    is_complete: bool = True

    def init(self, hws, cv):
        self.hws = hws
        self.cv = cv

    def complete(self) -> None:
        self.is_complete = True
        self.complete_cycle()

    def start_brewing(self) -> None:
        if self.hws.is_ready() and self.cv.is_ready():
            self.is_complete = False
            self.hws.start()
            self.cv.start()

    @abstractmethod
    def done(self) -> None:
        pass

    @abstractmethod
    def complete_cycle(self):
        pass
