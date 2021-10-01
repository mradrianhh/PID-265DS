from .component import Component

class Container(Component):
    __fluid_level: float # fluid level in meters

    def __init__(self, component: Component = None, tag: str = "", type: str = "", name: str = "", desc: str = "", fluid_level = 0):
        if component != None:
            super().__init__(component.get_tag(), component.get_type(), component.get_name(), component.get_desc())
        else:
            super().__init__(tag, type, name, desc)
        self.__fluid_level = fluid_level

    def get_fluid_level(self) -> float:
        return self.__fluid_level

    def set_fluid_level(self, fluid_level: float):
        self.__fluid_level = fluid_level