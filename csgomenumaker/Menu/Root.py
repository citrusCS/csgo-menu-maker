from .Menu import Menu
from .Folder import Folder


class Root(Folder):
    def __init__(self, parent, options):
        self.presetStore = {}
        self.isMenuRoot = True
        Folder.__init__(self, parent, options)
        self.cls = "menu-root"

    def joinChildren(self):
        max = len(self.selections)
        for i, ch in enumerate(self.selections):
            ch.setNeighbor("up", self.selections[(i - 1) % max])
            ch.setNeighbor("down", self.selections[(i + 1) % max])
            ch.setNeighbor("back", ch)
        for ch in self.selections:
            ch.joinChildren()

    def makeReAliases(self):
        for ch in self.selections:
            ch.makeReAliases()

    def addPreset(self, cls, name, preset):
        if cls not in self.presetStore.keys():
            self.presetStore[cls] = {}
        self.presetStore[cls][name] = preset

    def getPreset(self, cls, name):
        if cls not in self.presetStore.keys():
            self.error("No such preset type '%s'!" % cls)
        if name not in self.presetStore[cls].keys():
            self.error("No such preset named '%s' of type '%s'!" % (name, cls))
        return self.presetStore[cls][name]
