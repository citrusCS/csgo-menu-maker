from .. import Command
from .. import Misc

from .Menu import Menu


class Fireable(Menu):
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.command = None
        self.text = ""

    def setCommand(self, ref):
        self.command = ref

    def setText(self, text):
        self.text = text

    def makeChoices(self):
        horzSel = Command.NavState.Horz(self)
        horzSel.getAction("fire").getHook().addChild(self.command)
        self.addSelection(horzSel)
        textVar = "> %s <" % self.text
        horzSel.setTextContent(1, Misc.TextCenter(textVar, 40))
