from ..Compound import Compound

from .NavState import NavState
from .Horz import Horz


class VertFolder(NavState):
    def __init__(self, parent):
        NavState.__init__(self, parent)
        self.cls = "nav-vert-folder"
        self.dummy = Horz(self)
        self.getAction("fire").setHook(Compound(self.getAction("fire")))

    def joinChildren(self):
        self.dummy.setNeighbor("up", self.getNeighbor("up"))
        self.dummy.setNeighbor("down", self.getNeighbor("down"))
        self.dummy.setNeighbor("left", self.dummy)
        self.dummy.setNeighbor("right", self.dummy)
        self.dummy.setNeighbor("back", self.dummy)
        ec1 = self.dummy.getAction("fire").getHook()
        ec1 += self.getAction("fire").getHook()
        max = len(self.selections)
        for i, ch in enumerate(self.selections):
            ch.setNeighbor("up", self.selections[(i - 1) % max])
            ch.setNeighbor("down", self.selections[(i + 1) % max])
            ch.setNeighbor("back", self)
            ch.joinChildren()

    def makeReAliases(self):
        if hasattr(self, "error"):
            if len(self.selections) == 0:
                self.error("No selections present!")
        ec1 = self.getAction("entry").getHook()
        ec1 += self.dummy.getAction("entry").getHook()
        ec1 = self.getAction("fire").getHook()
        ec1 += self.selections[0].getAction("entry")
        self.dummy.makeReAliases()
        for ch in self.selections:
            ch.makeReAliases()

    def addSelection(self, ref):
        self.selections.append(ref)

    def getDummy(self):
        return self.dummy
