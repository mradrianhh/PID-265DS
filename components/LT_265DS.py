from .sensor import Sensor
from .container import Container

class LT_265DS(Sensor):

    def __init__(self, tag: str, variable: Container, name = "", desc = ""):
        super().__init__(variable, tag, name, desc)

    def read_pressure(self, density, gravitational_constant) -> float:
        return density * gravitational_constant * (Container)(self.__variable).get_fluid_level() 

    def get_name(self) -> str:
        return super().get_name()

    def get_tag(self) -> str:
        return super().get_tag()

    def get_desc(self) -> str:
        return super().get_desc()