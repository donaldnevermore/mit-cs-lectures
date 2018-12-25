from .coffee_maker_api import CoffeeMakerAPI
from .m4_user_interface import M4UserInterface
from .m4_hot_water_source import M4HotWaterSource
from .m4_containment_vessel import M4ContainmentVessel

api = CoffeeMakerAPI()
ui = M4UserInterface(api)
hws = M4HotWaterSource(api)
cv = M4ContainmentVessel(api)

ui.init(hws, cv)
hws.init(ui, cv)
cv.init(hws, ui)

while True:
    ui.poll()
    hws.poll()
    cv.poll()
