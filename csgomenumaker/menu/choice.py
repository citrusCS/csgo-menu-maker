from .. import command
from .. import misc

from .menu import Menu


class Choice(Menu):
    """
    Choose between different states for a specific option.
    """

    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.cls = "menu-choice"
        self.choices = []

    def add_choice(self, choicename, action, fire=None):
        """
        Add a (name, command action) object to the choice list.
        """
        self.choices.append((choicename, action, fire))

    def make_choices(self):
        """
        Generate the command.navstate.Horz objects necessary for this menu to
        function.
        """
        for i, ch in enumerate(self.choices):
            horz_sel = command.navstate.Horz(self)
            horz_sel.actions["entry"].hook.children.append(ch[1])
            if ch[2] != None:
                horz_sel.actions["fire"].hook.children.append(ch[2])
            self.selections.append(horz_sel)
            # Format is [val/max] // > selected <
            text_counter = "[%i/%i]" % (i+1, len(self.choices))
            text_name = "> %s <" % ch[0]
            horz_sel.text_contents[1] = misc.text_center(text_counter, 40)
            horz_sel.text_contents[2] = misc.text_center(text_name, 40)
