from ..realias import Realias

from .navstate import NavState


class Vert(NavState):
    """
    A vertical state transitioner.
    
    Vert instances are toggled between when you press up or down in the UI.
    """
    def __init__(self, parent):
        NavState.__init__(self, parent)
        self.cls = "nav-vert"
        
        # Dummy placeholder.
        self.dummy = None

    def join_children(self):
        """
        Set the neighbors of each child selection, so that make_realiases() can
        be run on them.
        """
        # Loop through each selection and set neighbors
        max = len(self.selections)
        for i, ch in enumerate(self.selections):
            ch.neighbors["up"] = self.neighbors["up"]
            ch.neighbors["down"] = self.neighbors["down"]
            # Clamp the selection index so that we can loop through. Fancy! B)
            ch.neighbors["left"] = self.selections[(i - 1) % max]
            ch.neighbors["right"] = self.selections[(i + 1) % max]
            ch.neighbors["back"] = self.neighbors["back"]

    def make_realiases(self):
        """
        Make all of the realiases on this instances' children. This function is
        called recursively.
        """
        # Raise an error if there aren't any selections. I'll support it at
        # some point. But not now.
        if len(self.selections) == 0:
            self.error("No selections present!")
        
        # Bind a default entry for the first element.
        entry_hook = self.actions["entry"].hook
        entry_hook += self.selections[0].actions["entry"].hook
        Realias(
            entry_hook,
            self.neighbors["back"].parent.actions["fire_back"],
            self.actions["entry"]
        )
            
        for ch in self.selections:
            ch.make_realiases()