from .Command import Command
from .Primitive import Primitive


class Color(Primitive):
    def __init__(self, parent, color):
        self.color = color
        Primitive.__init__(
            self,
            parent,
            "log_color",
            [
                "console",
                str(self.color)
            ]
        )
        self.cls = "primitive-color"
