from .. import Command

from .Menu import Menu
from .Fireable import Fireable


class FireableCmd(Fireable):
    def __init__(self, parent, options):
        Fireable.__init__(self, parent, options)
        self.setCommand(Command.Primitive(self, self.cmd, []))
        self.setText(self.cmd)
        self.makeChoices()
