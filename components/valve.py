from .actuator import Actuator
from .container import Container
from .direction import Direction

class Valve(Actuator):

    __position: float # position between 0-100%. 0% being closed.
    __max_flow_rate: float # flow rate in fully-open position(100%) in L/min.
    __max_flow_rate_si: float # flow rate in fully-open position given in SI-units, L/s.
    __direction: Direction

    """
    @param variable: The container the valve is attached to.
    @param position: Starting position of the valve. Defaults to fully closed.
    @param direction: Specifies whether it's an inlet or an outlet valve.
    """
    def __init__(self, variable: Container, actuator: Actuator = None, tag:str = "", name:str = "", desc:str = "", max_flow_rate: float = 10.0, position: float = 0.0, direction: Direction = Direction.INLET):
        if actuator != None:
            super().__init__(variable = actuator.get_variable(), tag = actuator.get_tag(), type = actuator.get_type(), name = actuator.get_name(), desc = actuator.get_desc())
        else:
            super().__init__(variable = variable, tag = tag, type = "actuator", name = name, desc = desc)

        self.__max_flow_rate = max_flow_rate
        self.__max_flow_rate_si = max_flow_rate / 60
        self.__position = position
        self.__direction = direction

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

    # Auxiliary functions

    def print_information(self):
        super().print_information()
        print(f'Direction: {self.__direction.name}')
        print(f'Max flowrate: {self.__max_flow_rate} L/min')
        print(f'Position: {self.__position}%')
        print(f'Current flowrate: {self.get_flow_rate()} L/min. Running at {self.get_flow_rate() * 100 / self.__max_flow_rate}% capacity.\n')

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


