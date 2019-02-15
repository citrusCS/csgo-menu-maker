from ..Command import Command
from ..Compound import Compound
from ..Placeholder import Placeholder


class NavState(Command):
    def __init__(self, parent):
        Command.__init__(self, parent, "nav")
        self.actions = {}
        self.neighbors = {}
        self.selections = []
        self.addAction("entry")
        self.getAction("entry").setHook(Compound(self.getAction("entry")))
        self.addAction("fire")
        self.uname = ""
        self.desc = ""
        self.sequence = 0
        self.sequenceCtr = 0
        if hasattr(self.parent, "sequenceCtr"):
            self.setSequence(self.parent.getSequenceCtr())
            self.parent.addSequenceCtr()

    def addAction(self, action):
        self.actions[action] = Placeholder(self, self.root.getGlobal("void"))

    def getAction(self, action):
        return self.actions[action]

    def setNeighbor(self, neighbor, ref):
        self.neighbors[neighbor] = ref

    def getNeighbor(self, neighbor):
        return self.neighbors[neighbor]

    def setUIName(self, uname):
        self.uname = uname

    def getUIName(self):
        return self.uname

    def setDesc(self, desc):
        self.desc = desc

    def getDesc(self):
        return self.desc

    def setSequence(self, n):
        self.sequence = n

    def getSequence(self):
        return self.sequence

    def getSequenceCtr(self):
        return self.sequenceCtr

    def addSequenceCtr(self):
        self.sequenceCtr += 1
