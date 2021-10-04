from .actuator import Actuator
from .container import Container

class Valve(Actuator):
    __position: float # position between 0-100%. 0% being closed.
    __max_flow_rate: float # flow rate in fully-open position(100%) in L/min.
    __max_flow_rate_si: float # flow rate in fully-open position given in SI-units, L/s.

    def __init__(self, variable: Container, actuator: Actuator = None, tag:str = "", name:str = "", desc:str = ""):
        if actuator != None:
            super().__init__(variable = actuator.get_variable(), tag = actuator.get_tag(), type = actuator.get_type(), name = actuator.get_name(), desc = actuator.get_desc())
        else:
            super().__init__(variable = variable, tag = tag, type = "actuator", name = name, desc = desc)

    """
    Set valve to failsafe position(closed).
    """
    def failsafe(self):
        self.__position = 0

    """
    Sets the position of the valve between 0%(closed) and 100%(open).

    @param position: position-value between 0-100.
    """
    def set_position(self, position: float):
        if position < 0 or position > 100:
            raise IndexError("position out of range. Approporiate values are 0-100.")
        else:
            self.__position = position

    """
    Calculate flowrate by linear-interpolation with regards to the max flowrate and the current position.
    If position is 50%, flowrate is 0.5 x max flowrate.
    """
    def get_flow_rate(self) -> float:
        return self.__position * self.__max_flow_rate

    def get_flow_rate_si(self) -> float:
        return self.__position * self.__max_flow_rate_si




    # Getters and setters

    def get_max_flow_rate(self) -> float:
        return self.__max_flow_rate

    def set_max_flow_rate(self, flow_rate: float):
        self.__max_flow_rate = flow_rate
        self.__max_flow_rate_si = flow_rate / 60

    def get_max_flow_rate_si(self) -> float:
        return self.__max_flow_rate_si

    def set_max_flow_rate_si(self, flow_rate: float):
        self.__max_flow_rate_si = flow_rate
        self.__max_flow_rate = flow_rate * 60


