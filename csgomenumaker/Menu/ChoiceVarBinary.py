from .Menu import Menu
from .ChoiceVar import ChoiceVar


class ChoiceVarBinary(ChoiceVar):
    default = 0

    def __init__(self, parent, options):
        ChoiceVar.__init__(self, parent, options)
        if self.default == 1:
            self.addChoice("1")
            self.addChoice("0")
        else:
            self.addChoice("0")
            self.addChoice("1")
        self.makeChoices()
