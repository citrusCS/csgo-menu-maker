from .Command import Command


class Placeholder(Command):
    def __init__(self, parent, hook):
        Command.__init__(self, parent, "placeholder")
        self.inherit = hook

    def setHook(self, ref):
        self.inherit = ref

    def getHook(self):
        return self.inherit

    def generate(self):
        return str(self.inherit)
