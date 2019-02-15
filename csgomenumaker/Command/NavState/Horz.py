from ..Compound import Compound
from ..Dialog import Dialog
from ..Realias import Realias

from .NavState import NavState


class Horz(NavState):
    def __init__(self, parent):
        NavState.__init__(self, parent)
        self.cls = "nav-horz"
        self.getAction("fire").setHook(Compound(self.getAction("fire")))
        self.addAction("display")
        self.dialog = Dialog(self.getAction("display"))
        self.getAction("display").setHook(self.dialog)
        self.textContents = ["", "", "", ""]
        self.desc = ""

    def makeReAliases(self):
        self.dialog.genDialog()
        ec1 = self.getAction("entry").getHook()
        ec1 += self.getAction("display").getHook()
        Realias(
            ec1,
            self.root.getGlobal("nav.up"),
            self.getNeighbor("up").getAction("entry")
        )
        Realias(
            ec1,
            self.root.getGlobal("nav.down"),
            self.getNeighbor("down").getAction("entry")
        )
        Realias(
            ec1,
            self.root.getGlobal("nav.left"),
            self.getNeighbor("left").getAction("entry")
        )
        Realias(
            ec1,
            self.root.getGlobal("nav.right"),
            self.getNeighbor("right").getAction("entry")
        )
        Realias(
            ec1,
            self.root.getGlobal("nav.fire"),
            self.getAction("fire").getHook()
        )
        Realias(
            ec1,
            self.root.getGlobal("nav.back"),
            self.getNeighbor("back").getAction("entry")
        )
        Realias(
            ec1,
            self.parent.getAction("entry").getHook(),
            self.getAction("entry")
        )
        Realias(
            ec1,
            self.root.getGlobal("nav.enable").getHook(),
            self.getAction("display")
        )
        if self.getNeighbor("back") != self:
            Realias(
                ec1,
                self.getNeighbor("back").getAction("fire").getHook(),
                self.getAction("entry")
            )

    def setTextContent(self, line, text):
        self.textContents[line] = text
