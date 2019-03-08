from ..command import Command
from ..compound import Compound
from ..placeholder import Placeholder


class NavState(Command):
    """
    Represents a UI navigation state, meaning that each instance of this is a
    separate point that one can be in the menu system.
    """
    def __init__(self, parent):
        Command.__init__(self, parent, "nav")
        
        # actions is a dict holding the commands executed upon entry or fire,
        # neighbors is a dict holding UI neighbors: like up, down, left, and
        # right - these are the states transitioned to on keypresses
        # selections is an array holding the children of this state that will
        # each be used
        self.actions = {}
        self.neighbors = {}
        self.selections = []
        
        # Create default actions
        self.actions["entry"] = Placeholder(self, self.root.globals["void"])
        self.actions["entry"].hook = Compound(self.actions["entry"])
        self.actions["fire"] = Placeholder(self, self.root.globals["void"])
        
        # UI parameters
        self.ui_name = ""
        self.desc = ""
        
        # Used for comparisons in Dialog
        self.sequence = 0
        self.sequence_ctr = 0
        if hasattr(self.parent, "sequence_ctr"):
            self.sequence = self.parent.sequence_ctr
            self.parent.sequence_ctr += 1

    # def addAction(self, action):
        # self.actions[action] = Placeholder(self, self.root.getGlobal("void"))

    # def getAction(self, action):
        # return self.actions[action]

    # def setNeighbor(self, neighbor, ref):
        # self.neighbors[neighbor] = ref

    # def getNeighbor(self, neighbor):
        # return self.neighbors[neighbor]

    # def setUIName(self, uname):
        # self.uname = uname

    # def getUIName(self):
        # return self.uname

    # def setDesc(self, desc):
        # self.desc = desc

    # def getDesc(self):
        # return self.desc

    # def setSequence(self, n):
        # self.sequence = n

    # def getSequence(self):
        # return self.sequence

    # def getSequenceCtr(self):
        # return self.sequenceCtr

    # def addSequenceCtr(self):
        # self.sequenceCtr += 1
