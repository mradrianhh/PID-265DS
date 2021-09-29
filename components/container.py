from .component import Component

class Container(Component):
    
    def __init__(self, name = "", desc = ""):
        self.__type = "container"
        self.__name = name
        self.__desc = desc