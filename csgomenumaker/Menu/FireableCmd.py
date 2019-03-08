from .. import command
from .. import param

from .menu import Menu
from .fireable import Fireable


class FireableCmd(Fireable):
    """
    Subclass of Fireable that runs a command.Primitive instead of an arbitrary
    command object.
    """
    def __init__(self, parent, options):
        Fireable.__init__(self, parent, options)
    
    def set_command(self, cmd):
        Fireable.set_command(self, [cmd,])
