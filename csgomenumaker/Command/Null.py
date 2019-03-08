from .command import Command


class Null(Command):
    """
    Null command; has no data other than that it does nothing.
    
    This is typically used as a sink for keybind actions.
    """
    def __init__(self, parent):
        Command.__init__(self, parent, "null")

    def generate(self):
        return ""
