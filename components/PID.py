from .controller import Controller
from .actuator import Actuator
from .sensor import Sensor
from .container import Container
from .loop import Loop

class PID(Controller):
    __gravitational_constant = 9.81
    __density = 981
    __loops: "dict[str, Loop]" = {}

    def __init__(self, tag: str, gravitational_constant: float = 9.81, density: float = 981, name = "", desc = ""):
        super().__init__(tag, name, desc)
        self.__gravitational_constant = gravitational_constant
        self.__density = density

    """
    @param loop: select the loop to simulate by tag.
    """
    def simulate(self, loop: str):
        pass

    def add_loop(self, tag: str, actuators: "dict[str, Actuator]" = {}, sensors: "dict[str, Sensor]" = {}):
        loop = Loop(self, tag, actuators, sensors)
        self.__loops[tag] = loop

    def get_loops(self) -> "dict[str, Loop]":
        return self.__loops

    def set_loops(self, loops: "dict[str, Loop]"):
        self.__loops = loops

    def get_loop(self, tag: str) -> Loop:
        return self.__loops[tag]

    def get_density(self) -> float:
        return self.__density

    def get_gravitational_constant(self) -> float:
        return self.__gravitational_constant