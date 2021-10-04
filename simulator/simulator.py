import time

class Simulator():
    __sample_rate: float
    __time_step: float # sample_rate converted for time.
    __simulating: bool

    def __init__(self, sample_rate: float = 1):
        self.__sample_rate = sample_rate
        self.__time_step = 1 / sample_rate

    def __execute(self):
        print("simulate")

    def __step(self):
        self.__execute()
        time.sleep(self.__time_step)

    def simulate(self):
        self.__simulating = True
        while(self.__simulating):
            self.__step()

