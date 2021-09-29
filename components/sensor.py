from .component import Component

class Sensor(Component):
    
    __variable: Component

    def __init__(self):
        self.__type = "sensor"

    def get_variable(self) -> str:
        return self.__variable.get_name