from .actuator import Actuator
from .container import Container

class Valve(Actuator):
    __state: str

    def __init__(self, variable: Container, actuator: Actuator = None, tag:str = "", name:str = "", desc:str = "", state:str = "CLOSED"):
        if actuator != None:
            super().__init__(variable = actuator.get_variable(), tag = actuator.get_tag(), type = actuator.get_type(), name = actuator.get_name(), desc = actuator.get_desc())
        else:
            super().__init__(variable = variable, tag = tag, type = "actuator", name = name, desc = desc)

        self.__state = state

    def open(self):
        self.__state = "OPEN"

    def close(self):
        self.__state = "CLOSED"