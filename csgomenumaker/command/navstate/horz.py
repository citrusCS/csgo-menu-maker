from ..compound import Compound
from ..dialog import Dialog
from ..placeholder import Placeholder
from ..realias import Realias

from .navstate import NavState


class Horz(NavState):
    """
    A horizontal state transitioner.

    Horz instances are toggled between when you press left or right in the UI.
    """

    def __init__(self, parent):
        NavState.__init__(self, parent)
        self.cls = "nav-horz"

        # Setup actions
        self.actions["fire"].hook = Compound(self.actions["fire"])
        self.actions["display"] = Placeholder(self, self.root.globals["void"])

        # Setup dialog on the display action, so that whenever this needs to be
        # displayed the dialog is shown
        self.dialog = Dialog(self.actions["display"])
        self.actions["display"].hook = self.dialog

        # text_contents holds the four lines shown in the dialog (typically, 2
        # are used but some menus use 4)
        self.text_contents = ["", "", "", ""]

        self.dummy = False

    def make_realiases(self):
        """
        Bind all neighbor commands to this state's actions. This is where the
        magic happens. I can't fully explain what is going on here.
        """
        # Make the dialog text
        self.dialog.generate_dialog()

        # Store a quick reference to the entry action, for more concise usage.
        entry_hook = self.actions["entry"].hook
        entry_hook.children.append(self.actions["display"].hook)

        # Make re-alias commands for each neighbor, and bind them to the entry
        # action hook.
        Realias(
            entry_hook,
            self.root.globals["nav.up"],
            self.neighbors["up"].actions["entry"]
        )
        Realias(
            entry_hook,
            self.root.globals["nav.down"],
            self.neighbors["down"].actions["entry"]
        )
        Realias(
            entry_hook,
            self.root.globals["nav.left"],
            self.neighbors["left"].actions["entry"]
        )
        Realias(
            entry_hook,
            self.root.globals["nav.right"],
            self.neighbors["right"].actions["entry"]
        )
        Realias(
            entry_hook,
            self.root.globals["nav.fire"],
            self.actions["fire"].hook
        )
        Realias(
            entry_hook,
            self.root.globals["nav.back"],
            self.neighbors["back"].actions["entry"]
        )
        Realias(
            entry_hook,
            self.parent.actions["entry"].hook,
            self.actions["entry"]
        )
        Realias(
            entry_hook,
            self.root.globals["nav.enable"].hook,
            self.actions["display"]
        )
