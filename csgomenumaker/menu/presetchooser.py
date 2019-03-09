from .. import command

from .menu import Menu
from .choice import Choice


class PresetChooser(Choice):
    """
    Choose between a set of presets in the menu.
    """

    def __init__(self, parent, options):
        Choice.__init__(self, parent, options)

    def add_preset(self, name, commands):
        """
        Add commands as the action for a preset of name 'name'.
        """
        ocmd = command.Compound(self)
        for cmd in commands:
            ocmd.children.append(cmd)
        self.add_choice(name, ocmd)
