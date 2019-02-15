from .Command import Command


class Null(Command):
    def __init__(self, parent):
        Command.__init__(self, parent, "null")

    def generate(self):
        return ""
