from .component import Component

class Controller(Component):

    def __init__(self, tag: str, name: str, desc: str):
        super().__init__(tag, "controller", name, desc)