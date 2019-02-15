from .NavState import NavState


class Vert(NavState):
    def __init__(self, parent):
        NavState.__init__(self, parent)
        self.cls = "nav-vert"

    def joinChildren(self):
        max = len(self.selections)
        for i, ch in enumerate(self.selections):
            ch.setNeighbor("up", self.getNeighbor("up"))
            ch.setNeighbor("down", self.getNeighbor("down"))
            ch.setNeighbor("left", self.selections[(i - 1) % max])
            ch.setNeighbor("right", self.selections[(i + 1) % max])
            ch.setNeighbor("back", self.getNeighbor("back"))

    def makeReAliases(self):
        if hasattr(self, "error"):
            if len(self.selections) == 0:
                self.error("No selections present!")
        ec1 = self.getAction("entry").getHook()
        ec1 += self.selections[0].getAction("entry").getHook()
        for ch in self.selections:
            ch.makeReAliases()

    def addSelection(self, ref):
        self.selections.append(ref)

    def getPath(self):
        if self.getNeighbor("back") == self:
            return "root/"+self.uname+"/"
        else:
            return self.getNeighbor("back").getPath()+self.uname+"/"

    def getPathDummy(self):
        if self.getNeighbor("back") == self:
            return "root/"
        else:
            return self.getNeighbor("back").getPath()+"/"

    def getDummy(self):
        return None
