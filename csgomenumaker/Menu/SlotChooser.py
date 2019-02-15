from .. import Command
from .. import Misc

from .Menu import Menu


class SlotChooser(Menu):
    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        self.slots = 0
        self.verb = ""

    def setSlots(self, slots):
        self.slots = slots

    def setVerb(self, verb):
        self.verb = verb

    def makeChoices(self):
        for i in range(self.slots):
            horzSel = Command.NavState.Horz(self)
            horzSel.getAction("fire").getHook().addChild(self.getCommand(i))
            self.addSelection(horzSel)
            textCounter = "%s slot [%i/%i]" % (self.verb, i+1, self.slots)
            maxTLen = len(str(self.slots))
            avgTLen = 4 + maxTLen + 3
            fstr = "%%0.%ii" % maxTLen
            outText = ""
            for j in range(0, 5):
                slotIdx = ((i + j)-2) % self.slots
                selText = ""
                if j == 2:
                    selText = self.root.boxDrawing[0b1010] + \
                        " > %s < " % str(slotIdx+1).rjust(maxTLen)
                else:
                    selText = self.root.boxDrawing[0b1010] + \
                        "   %s   " % str(slotIdx+1).rjust(maxTLen)
                outText += selText
            outText += self.root.boxDrawing[0b1010]
            damage = len(outText)-40
            if damage > 0:
                clip1 = damage//2
                clip2 = damage-clip1
                outText = outText[clip1:]
                outText = outText[:-clip2]
            horzSel.setTextContent(1, Misc.TextCenter(textCounter, 40))
            horzSel.setTextContent(2, outText)
