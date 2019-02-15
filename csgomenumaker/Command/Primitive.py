from .Command import Command


class Primitive(Command):
    def __init__(self, parent, concmd, args):
        Command.__init__(self, parent, "primitive")
        self.concmd = concmd
        if isinstance(args, list):
            self.args = list()
            self.args += args
        else:
            self.args = [args]

    def addArg(self, arg):
        self.args.append(arg)

    def generate(self):
        out = "%s" % self.concmd
        for arg in self.args:
            out += " %s" % str(arg)
        return out
