from .controller import Controller
from .actuator import Actuator
from .sensor import Sensor

class PID(Controller):
    __proportional_proportionality_factor: float # P
    __integral_proportionality_factor: float # I
    __differential_proportionality_factor: float # D

    __actuators: "list[Actuator]"
    __sensors: "list[Sensor]"

    def __init__(self, name = "", desc = ""):
        self.__name = name
        self.__desc = desc
        
    def add_actuator(self, actuator: Actuator):
        self.__actuators.append(actuator)

    def add_sensor(self, sensor: Sensor):
        self.__sensors.append(sensor)