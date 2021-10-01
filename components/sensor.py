from .component import Component

class Sensor(Component):
    
    __variable: Component

    def __init__(self, variable: Component, tag: str, name: str = "", desc: str = ""):
        super().__init__(tag, "sensor", name, desc)
        self.__variable = variable

    def get_variable(self) -> str:
        return self.__variable.get_name()