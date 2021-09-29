from .component import Component

class Container(Component):
    __fluid_level: float # fluid level in meters

    def __init__(self, tag: str, name = "", desc = "", fluid_level = 0):
        self.__type = "container"
        self.__name = name
        self.__desc = desc
        self.__tag = tag
        self.__fluid_level = fluid_level