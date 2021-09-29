from .sensor import Sensor
from .container import Container

class LT_265DS(Sensor):

    def __init__(self, tag: str, variable: Container, name = "", desc = ""):
        self.__name = name
        self.__desc = desc
        self.__tag = tag
        self.__variable = variable