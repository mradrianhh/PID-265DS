from .sensor import Sensor
from .container import Container

class LT_265DS(Sensor):

    def __init__(self, tag: str, variable: Container, name = "", desc = ""):
        self.__name = name
        self.__desc = desc
        self.__tag = tag
        self.__variable = variable

    def read_pressure(self, density, gravitational_constant) -> float:
        return density * gravitational_constant * (Container)(self.__variable).get_fluid_level() 

    def get_name(self) -> str:
        return self.__name

    def get_tag(self) -> str:
        return self.__tag

    def get_desc(self) -> str:
        return self.__desc