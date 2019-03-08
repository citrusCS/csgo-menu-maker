from ..compound import Compound
from ..placeholder import Placeholder
from ..primitive import Primitive

from .navstate import NavState
from .horz import Horz


class VertFolder(NavState):
    """
    A vertical state transitioner, that also holds recursive children.
    
    VertFolder instances are toggled between by pressing Back/Fire in the UI.
    """
    def __init__(self, parent):
        NavState.__init__(self, parent)
        self.cls = "nav-vert-folder"
        
        # self.dummy is a navstatehorz which serves as the UI element and 
        # inward transition for this navstate.
        self.dummy = Horz(self)
        self.dummy.dummy = True
        
        self.actions["fire"].hook = Compound(self.actions["fire"])
        self.actions["fire_back"] = Placeholder(self.actions["fire"].hook, self.root.globals["void"])
        self.actions["entry"].hook.children.append(self.dummy.actions["entry"].hook)
        self.dummy.actions["fire"].hook = self.actions["fire"]

    def join_children(self):
        """
        Set the neighbors of each child selection, so that make_realiases() can
        be run on them.
        """
        # Bind dummy to self neighbors.
        self.dummy.neighbors["up"] = self.neighbors["up"]
        self.dummy.neighbors["down"] = self.neighbors["down"]
        self.dummy.neighbors["left"] = self.dummy
        self.dummy.neighbors["right"] = self.dummy
        self.dummy.neighbors["back"] = self.neighbors["back"]
        
        if len(self.selections):
            self.actions["fire_back"].hook = self.selections[0].actions["entry"]
        
        # Setup the fire action - i.e. setup enter button press.
        max = len(self.selections)
        
        # Bind children selections to each other and self.
        for i, ch in enumerate(self.selections):
            ch.neighbors["up"] = self.selections[(i - 1) % max]
            ch.neighbors["down"] = self.selections[(i + 1) % max]
            ch.neighbors["back"] = self.dummy
            ch.join_children()

    def make_realiases(self):
        """
        Make all of the realiases on this instances' children. This function is
        called recursively.
        """
        #if len(self.selections) == 0:
        #    self.error("No selections present!")
        
        self.dummy.make_realiases()
        for ch in self.selections:
            ch.make_realiases()

    def get_path(self):
        """
        Return a path suitable for UI printing.
        """
        if self.parent is self.root:
            return "/"
        else:
            return self.parent.get_path()+self.ui_name+"/"
