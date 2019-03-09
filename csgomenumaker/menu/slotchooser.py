from .. import command
from .. import misc

from .menu import Menu


class SlotChooser(Menu):
    """
    Choose between different resource "buckets" (i.e. slots), and run a command
    based off of the one selected when the user presses fire. Also has a nice
    looking UI.
    """
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.slots = 0
        self.verb = ""

    def make_choices(self):
        """
        Generate the command.navstate.Horz objects necessary for this menu to
        function.
        """
        for i in range(self.slots):
            # Make the slot's horz object.
            horz_sel = command.navstate.Horz(self)
            horz_sel.actions["fire"].hook.children.append(self.get_command(i))
            self.selections.append(horz_sel)

            # Format the UI text for the object.
            text_counter = "%s slot [%i/%i]" % (self.verb, i+1, self.slots)
            max_t_len = len(str(self.slots))
            avg_t_len = 4 + max_t_len + 3
            fstr = "%%0.%ii" % max_t_len
            out_text = ""
            for j in range(0, 5):
                slot_idx = ((i + j)-2) % self.slots
                sel_text = ""
                if j == 2:
                    sel_text = self.root.box_drawing[0b1010] + \
                        " > %s < " % str(slot_idx+1).rjust(max_t_len)
                else:
                    sel_text = self.root.box_drawing[0b1010] + \
                        "   %s   " % str(slot_idx+1).rjust(max_t_len)
                out_text += sel_text
            out_text += self.root.box_drawing[0b1010]
            damage = len(out_text)-40
            if damage > 0:
                clip1 = damage//2
                clip2 = damage-clip1
                out_text = out_text[clip1:]
                out_text = out_text[:-clip2]
            horz_sel.text_contents[1] = misc.text_center(text_counter, 40)
            horz_sel.text_contents[2] = out_text
