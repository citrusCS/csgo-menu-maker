from .. import Command
from .. import Misc

from .Menu import Menu


class Choice(Menu):
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.cls = "menu-choice"
        self.choices = []

    def addChoice(self, choicename, action):
        self.choices.append((choicename, action))

    def makeChoices(self):
        for i, ch in enumerate(self.choices):
            horzSel = Command.NavState.Horz(self)
            horzSel.getAction("entry").getHook().addChild(ch[1])
            self.addSelection(horzSel)
            textCounter = "[%i/%i]" % (i+1, len(self.choices))
            textName = "> %s <" % ch[0]
            horzSel.setTextContent(1, Misc.TextCenter(textCounter, 40))
            horzSel.setTextContent(2, Misc.TextCenter(textName, 40))
