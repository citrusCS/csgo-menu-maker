from .. import Command
from .. import Misc

from .Menu import Menu


class ChoiceVar(Menu):
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.cls = "menu-choice-var"
        self.choices = []

    def setVar(self, var):
        self.var = var

    def addChoice(self, varValue):
        self.optType(varValue, str())
        self.choices.append(varValue)

    def makeChoices(self):
        if len(self.choices) == 0:
            self.error("Not enough choices for convar '%s'" % self.var)
        for i, ch in enumerate(self.choices):
            horzSel = Command.NavState.Horz(self)
            horzSel.getAction("entry").getHook().addChild(
                Command.Primitive(
                    self,
                    self.var,
                    ch
                )
            )
            self.addSelection(horzSel)
            textVar = "%s %s" % (self.var, ch)
            textChoice = ""
            if len(self.choices) == 2:
                if i == 0:
                    textChoice = "> %s < %s   %s  " % \
                        (
                            self.choices[0],
                            self.root.boxDrawing[0b1010],
                            self.choices[1]
                        )
                elif i == 1:
                    textChoice = "  %s   %s > %s <" % \
                        (
                            self.choices[0],
                            self.root.boxDrawing[0b1010],
                            self.choices[1]
                        )
            else:
                textChoice = "> %s <" % ch
            horzSel.setTextContent(1, Misc.TextCenter(textVar, 40))
            horzSel.setTextContent(2, Misc.TextCenter(textChoice, 40))
