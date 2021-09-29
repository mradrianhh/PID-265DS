from .actuator import Actuator

class Valve(Actuator):
    __state: str

    def __init__(self, name = "", desc = "", state = "CLOSED"):
        self.__type = "actuator"
        self.__state = state
        self.__name = name
        self.__desc = desc

    def open(self):
        self.__state = "OPEN"

    def close(self):
        self.__state = "CLOSED"