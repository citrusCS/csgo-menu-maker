from .Command import Command
from .File import File


class Indirect(Command):
    def __init__(self, parent):
        Command.__init__(self, parent, "indirect")
        self.container = File(self)
        self.hideChildren = True

    def generate(self):
        for cmd in self.children:
            if cmd == self.container:
                continue
            line = cmd.generate()
            self.container.addLine(line)
        return "exec " + str(self.container)
