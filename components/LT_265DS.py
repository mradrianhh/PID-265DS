from .sensor import Sensor
from .container import Container
from .component import Component

class LT_265DS(Sensor):
    __density: float = 981
    __gravitational_constant: float = 9.81

    def __init__(self, variable: Component, tag: str = "", name: str = "", desc: str = "", sensor: Sensor = None):
        if sensor != None:
            super().__init__(sensor.get_variable(), type = sensor.get_type(), tag = sensor.get_tag(), name = sensor.get_name(), desc = sensor.get_desc())
        else:
            super().__init__(variable, tag = tag, type = "sensor", name = name, desc = desc)

    def read_pressure(self) -> float:
        return self.__density * self.__gravitational_constant * Container(self.get_variable()).get_fluid_level()

    def read_fluid_level(self) -> float:
        return Container(self.get_variable()).get_fluid_level()

    def print_information(self):
        super().print_information()
        print(f'Pressure: {self.read_pressure()}\n')