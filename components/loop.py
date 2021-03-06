from .actuator import Actuator
from .sensor import Sensor

class Loop(object):
        __tag: str
        __actuators: "dict[str, Actuator]"
        __sensors: "dict[str, Sensor]"
        __target_value: float = 0.0
        __actual_value: float = 0.0
        __error: float # target_value - actual_value
        __proportional_proportionality_factor: float
        __integral_proportionality_factor: float
        __differential_proportionality_factor: float

        def __init__(self, tag: str, actuators: "dict[str, Actuator]" = [], sensors: "dict[str, Sensor]" = [], proportional_proportionality_factor: float = 0.0, integral_proportionality_factor: float = 0.0, differential_proportionality_factor: float = 0.0):
            self.__actuators = actuators
            self.__sensors = sensors
            self.__tag = tag
            self.__proportional_proportionality_factor = proportional_proportionality_factor
            self.__integral_proportionality_factor = integral_proportionality_factor
            self.__differential_proportionality_factor = differential_proportionality_factor

        def calculate_error(self):
            self.__error = self.__target_value - self.__actual_value

        def calculate_proportional(self) -> float:
            return self.__error * self.__proportional_proportionality_factor

        def print_information(self):
            print(self.__tag)
            print(f'Target value : {self.__target_value}')
            print(f'Actual value: {self.__actual_value}')
            print("Actuators:")
            for key in self.__actuators.keys():
                print(f'\t{key} : {self.__actuators[key].get_desc()}')
            print("Sensors:")
            for key in self.__sensors.keys():
                print(f'\t{key} : {self.__sensors[key].get_desc()}')

        def add_actuator(self, actuator: Actuator):
            self.__actuators[actuator.get_tag()] = actuator

        def add_sensor(self, sensor: Sensor):
            self.__sensors[sensor.get_tag()] = sensor

        def get_target_value(self) -> float:
            return self.__target_value

        def set_target_value(self, target_value: float):
            self.__target_value = target_value

        def get_actual_value(self) -> float:
            return self.__actual_value

        def set_actual_value(self, actual_value: float):
            self.__actual_value = actual_value

        def get_actuators(self) -> "dict[str, Actuator]":
            return self.__actuators

        def get_actuator(self, key) -> Actuator:
            return self.__actuators[key]

        def get_sensors(self) -> "dict[str, Sensor]":
            return self.__sensors

        def get_sensor(self, key) -> Sensor:
            return self.__sensors[key]

        def get_proportional_proportionality_factor(self) -> float:
            return self.__proportional_proportionality_factor
    
        def set_proportional_proportionality_factor(self, proportional_proportionality_factor: float):
            self.__proportional_proportionality_factor = proportional_proportionality_factor

        def get_integral_proportionality_factor(self) -> float:
            return self.__integral_proportionality_factor

        def set_integral_proportionality_factor(self, integral_proportionality_factor: float):
            self.__integral_proportionality_factor = integral_proportionality_factor

        def get_differential_proportionality_factor(self) -> float:
            return self.__differential_proportionality_factor

        def set_differential_proportionality_factor(self, differential_proportionality_factor: float):
            self.__differential_proportionality_factor = differential_proportionality_factor

        def get_error(self) -> float:
            return self.__error

        def set_error(self, error: float):
            self.__error = error
