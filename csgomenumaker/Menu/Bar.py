from .. import Command
from .. import Misc

from .Menu import Menu


class Bar(Menu):
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.cls = "menu-bar"
        self.min = 0
        self.max = 0
        self.steps = 0
        self.var = ""
        self.style = "percent"
        self.default = self.max

    def setMin(self, min):
        self.min = min

    def setMax(self, max):
        self.max = max

    def setSteps(self, steps):
        self.steps = steps

    def setStyle(self, style):
        self.style = style

    def setVar(self, var):
        self.var = var

    def setDefault(self, default):
        self.default = default

    def makeChoices(self):
        stepAmt = (self.max-self.min)/self.steps
        stepVal = (self.default-self.min)
        self.default = int(
            (stepAmt * round(float(stepVal)/stepAmt) * (1/stepAmt))
        )
        for i in range(self.steps+1):
            horzSel = Command.NavState.Horz(self)
            fract = ((i+self.default) % (self.steps+1))/self.steps
            val = Misc.lerp(self.min, self.max, fract)
            horzSel.getAction("entry").getHook().addChild(
                Command.Primitive(
                    self,
                    self.var,
                    [val]
                )
            )
            self.addSelection(horzSel)
            textBlocks = self.root.blockChar * (int(fract*30)) + \
                " "*(30-int(fract*30))
            textBar = self.root.boxDrawing[0b1010] + textBlocks + \
                self.root.boxDrawing[0b1010]
            textBarPerc = ""
            textBarLabel = ""
            if self.style == "percent":
                percVal = "%i%%" % int(val*100)
                textBarPerc = percVal.rjust(5)
                textBarLabelMin = str(int(self.min*100))
                textBarLabelMax = str(int(self.max*100))
            elif self.style == "int":
                textBarPerc = ("%i" % val).rjust(5)
                textBarLabelMin = "%i" % self.min
                textBarLabelMax = "%i" % self.max
            textBar = textBarPerc + " " + textBar + "  "
            spc = 30
            spc -= len(textBarLabelMin)
            spc -= len(textBarLabelMax)
            textBarLabel = "       " + textBarLabelMin + (" "*spc) + \
                textBarLabelMax + "   "
            horzSel.setTextContent(1, textBar)
            horzSel.setTextContent(2, textBarLabel)
