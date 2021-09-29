from .sensor import Sensor

class LT_265DS(Sensor):

    def __init__(self, name = "", desc = ""):
        self.__name = name
        self.__desc = desc