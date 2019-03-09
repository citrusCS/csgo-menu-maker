import math

from .. import command
from .. import misc

from .menu import Menu


class Message(Menu):
    """
    Show a static message.
    """

    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.text = ""

    # def setText(self, text):
        # self.text = text

    def make_choices(self):
        """
        Generate the command.navstate.Horz objects necessary for this menu to
        function.
        """
        # Sanitize all of the lines for "special" characters (read: some C0
        # controls) before anything is done with them.
        lines = self.text.split("\n")
        if len(lines) == 0:
            self.error("Text cannot be empty!")
        for i, line in enumerate(lines):
            lines[i] = line.replace("\r", "")
            lines[i] = line.replace("\b", "")
            lines[i] = line.replace("\"", "")
            lines[i] = line.replace("\t", "    ")

        # Word wrap each line and place it into a list.
        total_lines = []
        for i, line in enumerate(lines):
            total_lines.extend(misc.text_word_wrap(line, 40))

        # Split total_lines into a set of pages, with each page having four
        # wrapped lines.
        pages = math.ceil(len(total_lines) / 4)
        for i in range(pages):
            horz_sel = command.navstate.Horz(self)
            self.selections.append(horz_sel)
            for j in range(4):
                idx = (i * 4) + j
                if idx >= len(total_lines):
                    continue
                text = total_lines[idx]
                horz_sel.text_contents[j] = text
