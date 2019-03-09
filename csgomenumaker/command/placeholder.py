from .command import Command


class Placeholder(Command):
    """
    An command that holds an overwritable reference to another command.

    It is used for most UI navigation, in order to rebind navigation keys to
    other values.
    """

    def __init__(self, parent, hook):
        Command.__init__(self, parent, "placeholder")

        # hook is the command that will get overwritten.
        self.hook = hook

    def generate(self):
        return str(self.hook)
