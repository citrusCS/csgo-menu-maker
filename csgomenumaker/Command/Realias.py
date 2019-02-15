from .Command import Command


class Realias(Command):
    def __init__(self, parent, dest, src):
        Command.__init__(self, parent, "realias")
        self.dest = dest
        self.src = src
        self.clean = True

    def generate(self):
        return "alias " + str(self.dest) + " " + str(self.src)
