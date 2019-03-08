from .menu import Menu
from .choicevar import ChoiceVar


class ChoiceVarBinary(ChoiceVar):
    """
    Subclass of ChoiceVar only enabling two states: 0 and 1.
    """
    
    def __init__(self, parent, options):
        ChoiceVar.__init__(self, parent, options)
    
    def make_choices(self):
        # Swap choices if the default is 1. However 90% of the time, it is not.
        if self.default == 1:
            self.add_choice("1")
            self.add_choice("0")
        else:
            self.add_choice("0")
            self.add_choice("1")
        ChoiceVar.make_choices(self)
