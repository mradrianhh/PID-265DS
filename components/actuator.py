from .component import Component

class Actuator(Component):
    __variable: Component
    
    def __init__(self):
        self.__type = "actuator"

    def get_variable(self) -> str:
        return self.__variable.get_name