import sys

from .screen_interface import ScreenInterface

class MainOverview(ScreenInterface):

    def show(self):
        print("Main overview\n")
        print("(1) View loops - (2) View actuators - (3) View sensors - (4) View sensors - (0) Exit")

        response = input()
        sys.exit(0)