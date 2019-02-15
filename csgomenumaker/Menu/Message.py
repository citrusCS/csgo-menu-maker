import math

from .. import Command
from .. import Misc

from .Menu import Menu


class Message(Menu):
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.text = ""

    def setText(self, text):
        self.text = text

    def makeChoices(self):
        lines = self.text.split("\n")
        self.optLenZeroName(lines, self.text)
        for i, line in enumerate(lines):
            lines[i] = line.replace("\r", "")
            lines[i] = line.replace("\b", "")
            lines[i] = line.replace("\"", "")
            lines[i] = line.replace("\t", "    ")
        totalLines = []
        for i, line in enumerate(lines):
            totalLines += Misc.TextWordWrap(line, 40)
        pages = math.ceil(len(totalLines) / 4)
        for i in range(pages):
            horzSel = Command.NavState.Horz(self)
            self.addSelection(horzSel)
            for j in range(4):
                idx = (i * 4) + j
                if idx >= len(totalLines):
                    continue
                text = totalLines[idx]
                horzSel.setTextContent(j, text)
