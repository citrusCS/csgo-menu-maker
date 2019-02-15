from .. import Misc

from .Command import Command
from .Compound import Compound
from .Echo import Echo
from .Indirect import Indirect


class Dialog(Compound):
    def __init__(self, parent):
        Compound.__init__(self, parent)
        self.cls = "dialog"
        self.horzpar = self.parent.parent

    def getNeighbors(self):
        self.neighbor0 = self.horzpar.getNeighbor("up")
        self.neighbor1 = self.horzpar.parent
        self.neighbor2 = self.horzpar.getNeighbor("down")
        self.neighbor3 = self.horzpar.getNeighbor("down").getNeighbor("down")
        if self.neighbor0.getSequence() >= self.neighbor1.getSequence():
            self.neighbor0_text = ""
        else:
            self.neighbor0_text = self.neighbor0.getUIName()
        self.neighbor1_text = self.neighbor1.getUIName()
        if self.neighbor2.getSequence() <= self.neighbor1.getSequence():
            self.neighbor2_text = ""
        else:
            self.neighbor2_text = self.neighbor2.getUIName()
        if self.neighbor3.getSequence() <= self.neighbor1.getSequence():
            self.neighbor3_text = ""
        else:
            self.neighbor3_text = self.neighbor3.getUIName()

    def formatHeader(self):
        backn = self.horzpar.getNeighbor("back")
        if backn.cls == "nav-horz":
            backn = backn.parent
        text = backn.getPath()
        if backn.getDummy() == self.horzpar:
            text = backn.getPathDummy()
        header = self.root.boxDrawing[0b0011]
        header += self.root.boxDrawing[0b0101]*2
        header += self.root.boxDrawing[0b1110]
        header += " "
        header += Misc.TextExtend(text, 70, self.root.padChar)
        header += " "
        header += self.root.boxDrawing[0b1011]
        header += self.root.boxDrawing[0b0101]*2
        header += self.root.boxDrawing[0b0110]
        return header

    def formatContents0(self):
        horzText = self.horzpar.textContents[0]
        return self.formatContentsOther(self.neighbor0_text, horzText)

    def formatContents1(self):
        vertText = self.neighbor1_text
        vertText = Misc.TextRestrict(vertText, 25)
        vertText = Misc.TextCenter("> " + vertText + " < ", 30)
        horzText = self.horzpar.textContents[1]
        horzText = Misc.TextExtend(horzText, 40)
        outText = vertText + self.root.boxDrawing[0b1010] + " " + horzText
        return self.formatContentsGeneric(outText)

    def formatContents2(self):
        horzText = self.horzpar.textContents[2]
        return self.formatContentsOther(self.neighbor2_text, horzText)

    def formatContents3(self):
        horzText = self.horzpar.textContents[3]
        return self.formatContentsOther(self.neighbor3_text, horzText)

    def formatContentsOther(self, vertText, horzText):
        vertText = Misc.TextRestrict(vertText, 25)
        vertText = Misc.TextCenter("  " + vertText + "   ", 30)
        horzText = Misc.TextExtend(horzText, 40)
        outText = vertText + self.root.boxDrawing[0b1010] + " " + horzText
        return self.formatContentsGeneric(outText)

    def formatContentsGeneric(self, text):
        outText = self.root.boxDrawing[0b1010]
        outText += "  "
        outText += text
        outText += "    "
        outText += self.root.boxDrawing[0b1010]
        return outText

    def formatFooter(self):
        text = self.horzpar.parent.getDesc()
        footer = self.root.boxDrawing[0b1001]
        footer += self.root.boxDrawing[0b0101]*2
        footer += self.root.boxDrawing[0b1110]
        footer += " "
        footer += Misc.TextExtend(text, 70, " ")
        footer += " "
        footer += self.root.boxDrawing[0b1011]
        footer += self.root.boxDrawing[0b0101]*2
        footer += self.root.boxDrawing[0b1100]
        return footer

    def formatKey(self, keybind):
        kbs = self.root.config.keybinds
        return "[%s]" % kbs[keybind].upper()

    def genDialog(self):
        self.getNeighbors()
        help0 = self.formatKey("up") + " / " + self.formatKey("down") \
            + " - Previous/Next"
        help1 = self.formatKey("left") + " / " + self.formatKey("right") \
            + " - Change Setting"
        help2 = self.formatKey("fire") + " - Enter Folder / Run Command"
        help3 = self.formatKey("back") + " - Exit Folder"
        line0 = self.formatHeader()
        line1 = self.formatContents0() + " " + help0
        line2 = self.formatContents1() + " " + help1
        line3 = self.formatContents2() + " " + help2
        line4 = self.formatContents3() + " " + help3
        line5 = self.formatFooter()
        indir = Indirect(self)
        Echo(indir, line0)
        Echo(indir, line1)
        Echo(indir, line2)
        Echo(indir, line3)
        Echo(indir, line4)
        Echo(indir, line5)
