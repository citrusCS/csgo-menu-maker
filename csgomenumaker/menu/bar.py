from .. import command
from .. import misc

from .menu import Menu


class Bar(Menu):
    """
    Renders a nice-looking "slider"-style bar in the navigation window.
    """

    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.cls = "menu-bar"
        self.min = 0             # minimum value
        self.max = 0             # maximum value
        self.steps = 0           # steps from min - max
        self.var = ""            # var to change in the operation
        self.style = "int"       # label style
        self.default = self.max  # default value to start at

    def make_choices(self):
        """
        Generate the command.navstate.Horz objects necessary for this menu to
        function.
        """
        # Clamp self.default to a multiple of the amount between steps.
        step_amt = (self.max-self.min)/self.steps
        step_val = (self.default-self.min)
        self.default = int(
            (step_amt * round(float(step_val)/step_amt) * (1/step_amt))
        )

        # Generate each horz selection.
        for i in range(self.steps+1):
            # Add the selection and a command.
            horz_sel = command.navstate.Horz(self)
            fract = ((i+self.default) % (self.steps+1))/self.steps
            val = misc.lerp(self.min, self.max, fract)
            horz_sel.actions["entry"].hook.children.append(
                self.make_cmd(
                    self.var,
                    val
                )
            )
            self.selections.append(horz_sel)

            # Generate the text for each line of the navigation window.
            text_blocks = self.root.block_char * (int(fract*30)) + \
                " "*(30-int(fract*30))
            text_bar = self.root.box_drawing[0b1010] + text_blocks + \
                self.root.box_drawing[0b1010]
            text_bar_perc = ""
            text_bar_label = ""
            if self.style == "percent":
                perc_val = "%i%%" % int(val*100)
                text_bar_perc = perc_val.rjust(5)
                text_bar_label_min = str(int(self.min*100))
                text_bar_label_max = str(int(self.max*100))
            elif self.style == "int":
                text_bar_perc = ("%i" % val).rjust(5)
                text_bar_label_min = "%i" % self.min
                text_bar_label_max = "%i" % self.max
            elif self.style == "str":
                text_bar_perc = ("%i" % val).rjust(5)
                text_bar_label_min = self.strleft
                text_bar_label_max = self.strright
            text_bar = text_bar_perc + " " + text_bar + "  "
            spc = 30
            spc -= len(text_bar_label_min)
            spc -= len(text_bar_label_max)
            text_bar_label = "       " + text_bar_label_min + (" "*spc) + \
                text_bar_label_max + "   "
            horz_sel.text_contents[1] = text_bar
            horz_sel.text_contents[2] = text_bar_label
