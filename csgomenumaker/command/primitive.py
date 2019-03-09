from .command import Command


class Primitive(Command):
    """
    Stores a single console command, and does not point to an alias.

    Used to run arbitrary console commands.
    """

    def __init__(self, parent, concmd, args):
        Command.__init__(self, parent, "primitive")

        # concmd is the name of the console command, args is a list of
        # arguments
        self.concmd = concmd

        # args may be passed as a list or string
        if isinstance(args, list):
            self.args = list()
            self.args.extend(args)
        else:
            self.args = [args, ]

    def generate(self):
        # Concatenate self.concmd with self.args.
        out = str(self.concmd) \
            + " " + " ".join([str(arg) for arg in self.args])
        return out
