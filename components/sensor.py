from .component import Component

class Sensor(Component):
    
    __variable: Component

    def __init__(self, variable: Component, component: Component = None, tag: str = "", type: str = "", name: str = "", desc: str = ""):
        if component != None:
            super().__init__(component.get_tag(), component.get_type(), component.get_name(), component.get_desc())
        else:
            super().__init__(tag, type, name, desc)
        self.__variable = variable

    def get_variable(self) -> str:
        return self.__variable