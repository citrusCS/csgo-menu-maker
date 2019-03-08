from .. import command
from .. import misc

from .menu import Menu


class Fireable(Menu):
    """
    Menu object that runs an action when the user presses the Fire key while
    selecting it.
    """
    
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.command = None
        self.text = ""

    def set_command(self, cmds):
        self.command = command.Compound(self)
        for cmd in cmds:
            command.Primitive(self.command, cmd, [])

    # def setCommand(self, ref):
        # self.command = ref

    # def setText(self, text):
        # self.text = text

    def make_choices(self):
        """
        Generate the command.navstate.Horz objects necessary for this menu to
        function.
        """
        # Create the horz object and bind the fire action to it.
        horz_sel = command.navstate.Horz(self)
        horz_sel.actions["fire"].hook.children.append(self.command)
        self.selections.append(horz_sel)
        
        # Make the UI text.
        text_var = "> %s <" % self.text
        horz_sel.text_contents[1] = misc.text_center(text_var, 40)
