from components import *

PID = PID("PID_01", name = "PID_01", desc = "Controller for fluid level control.")

T_2 = Container(tag = "T-2", type = "container", name = "T-2", desc = "Mixing tank in soda-factory.")

LT = LT_265DS(name = "LT_01", variable = T_2, tag = "LT_01", type = "sensor", desc = "Differential pressure sensor for measuring fluid level in T-2.")

VALVE = Valve(name = "V_01", variable = T_2, tag = "V_01", desc = "Water valve for T-2.")

PID.add_actuator(VALVE)

PID.add_sensor(LT)

PID.add_loop("FLUID_LEVEL_T_2", ["V_01"], ["LT_01"])

PID.get_loop("FLUID_LEVEL_T_2").print_information()