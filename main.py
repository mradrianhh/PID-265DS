from components import *

PID = PID("PID_01", name = "PID_01", desc = "Controller for fluid level control.")

T_2 = Container("T-2", "T-2", "Mixing tank in soda-factory.")

LT = LT_265DS("LT_01", T_2, "LT_01", "Differential pressure sensor for measuring fluid level in T-2.")

VALVE = Valve("V_01", T_2, "V_01", "Water valve for T-2.")

PID.add_actuator(VALVE)

PID.add_sensor(LT)

PID.add_loop("FLUID_LEVEL_T_2", ["V_01"], ["LT_01"])

PID.get_loop("FLUID_LEVEL_T_2").print_information()