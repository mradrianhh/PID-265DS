from .sensor import Sensor
from .container import Container
from .component import Component

class LT_265DS(Sensor):

    def __init__(self, sensor: Sensor = None, variable: Component = None, type: str = "", tag: str = "", name: str = "", desc: str = ""):
        if sensor != None:
            super().__init__(sensor.get_variable(), type = sensor.get_type(), tag = sensor.get_tag(), name = sensor.get_name(), desc = sensor.get_desc())
        else:
            super().__init__(variable, tag = tag, type = type, name = name, desc = desc)

    def read_pressure(self, density, gravitational_constant) -> float:
        return density * gravitational_constant * Container(self.get_variable()).get_fluid_level()