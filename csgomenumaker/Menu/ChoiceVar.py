from .. import command
from .. import misc

from .menu import Menu


class ChoiceVar(Menu):
    """
    Similar to Choice, except functions as a shortcut, only allowing variable
    changes rather than an arbitrary command instance.
    """
    
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.cls = "menu-choice-var"
        self.choices = []

    def add_choice(self, var_value):
        """
        Add a (variable, state) object to the choice list.
        """
        self.choices.append(var_value)

    def make_choices(self):
        """
        Generate the command.navstate.Horz objects necessary for this menu to
        function.
        """
        # No support for 0 choices.
        if len(self.choices) == 0:
            self.error("Not enough choices for convar/cmd '%s'" % self.var)
        
        # Generate each command.navstate.Horz object.
        for i, ch in enumerate(self.choices):
            # Make the actual object, and make its convar command.Primitive as
            # well.
            horz_sel = command.navstate.Horz(self)
            horz_sel.actions["entry"].hook.children.append(
                command.Primitive(
                    self,
                    self.var,
                    ch
                )
            )
            self.selections.append(horz_sel)
            # Make the text shown in the UI.
            text_var = "%s %s" % (self.var, ch)
            text_choice = ""
            if len(self.choices) == 2:
                if i == 0:
                    text_choice = "> %s < %s   %s  " % \
                        (
                            self.choices[0],
                            self.root.box_drawing[0b1010],
                            self.choices[1]
                        )
                elif i == 1:
                    text_choice = "  %s   %s > %s <" % \
                        (
                            self.choices[0],
                            self.root.box_drawing[0b1010],
                            self.choices[1]
                        )
            else:
                text_choice = "> %s <" % ch
            horz_sel.text_contents[1] = misc.text_center(text_var, 40)
            horz_sel.text_contents[2] = misc.text_center(text_choice, 40)
