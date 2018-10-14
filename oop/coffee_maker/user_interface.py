class UserInterface:
    hws: HotWaterSouce
    cv: ContainmentVessel

    def done(self) -> None:
        pass

    def complete(self) -> None:
        pass

    def start_brewing(self) -> None:
        if hws.is_ready() and cv.is_ready():
            hws.start()
            cv.start()
