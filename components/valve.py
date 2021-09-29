from .actuator import Actuator
from .container import Container

class Valve(Actuator):
    __state: str

    def __init__(self, tag: str, variable: Container, name = "", desc = "", state = "CLOSED"):
        self.__type = "actuator"
        self.__state = state
        self.__name = name
        self.__desc = desc
        self.__tag = tag
        self.__variable = variable

    def open(self):
        self.__state = "OPEN"

    def close(self):
        self.__state = "CLOSED"

    def get_name(self) -> str:
        return self.__name

    def get_tag(self) -> str:
        return self.__tag