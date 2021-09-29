from components import *

PID = PID("PID_01", "Controller 1", "Controller for fluid level regulation.")

T_2 = Container("T-2", "T-2", "Mixing tank in soda-factory.")

LT = LT_265DS("LT_01", T_2, "LT_01", "Differential pressure sensor for measuring fluid level in T-2.")

VALVE = Valve("V_01", T_2, "V_01", "Water valve for T-2.")

PID.add_actuator(VALVE)

PID.add_sensor(LT)

for actuator in [PID.get_actuators()[key] for key in PID.get_actuators().keys()]:
    print(actuator.get_name())
    print(actuator.get_tag())

for sensor in [PID.get_sensors()[key] for key in PID.get_sensors().keys()]:
    print(sensor.get_name())
    print(sensor.get_tag())

PID.add_loop("FLUID_LEVEL_T_2", ["V_01"], ["LT_01"])

PID.get_loop("FLUID_LEVEL_T_2").print_information()