"""
from components import *

PID = PID(tag = "PID_01", name = "PID_01", desc = "Controller for fluid level control.")
T_2 = Container(tag = "T-2", type = "container", name = "T-2", desc = "Mixing tank in soda-factory.")

LT = LT_265DS(name = "LT_01", variable = T_2, tag = "LT_01", type = "sensor", desc = "Differential pressure sensor for measuring fluid level in T-2.")

VALVE = Valve(name = "V_01", variable = T_2, tag = "V_01", desc = "Water valve for T-2.")

PID.add_loop("FLUID_LEVEL_T_2")

loop = PID.get_loop("FLUID_LEVEL_T_2")

loop.add_actuator(VALVE)
loop.add_sensor(LT)

loop.print_information()"""

from simulator import Simulator

sim = Simulator()
sim.simulate()