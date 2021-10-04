from .controller import Controller
from .actuator import Actuator
from .sensor import Sensor
from .container import Container
from .loop import Loop

class PID(Controller):
    __loops: "dict[str, Loop]" = {}

    def __init__(self, tag: str, name = "", desc = ""):
        super().__init__(tag, name, desc)

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