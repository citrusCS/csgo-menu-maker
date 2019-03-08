from .menu import Menu
from .folder import Folder


class Root(Folder):
    """
    Root menu object.
    
    Always the first Menu subclass initialized. Also, holds global
    PresetChooser presets.
    """
    
    def __init__(self, parent, options):
        self.preset_store = {}
        self.preset_cmd_store = {}
        self.is_menu_root = True
        Folder.__init__(self, parent, options)
        self.cls = "menu-root"

    def join_children(self):
        """
        Override of navstate's join_children implementation to not link back
        neighbors, as there are none!
        """
        self.neighbors["back"] = self
        max = len(self.selections)
        for i, ch in enumerate(self.selections):
            ch.neighbors["up"] = self.selections[(i - 1) % max]
            ch.neighbors["down"] = self.selections[(i + 1) % max]
            ch.neighbors["back"] = ch
        for ch in self.selections:
            ch.join_children()

    def make_realiases(self):
        """
        Override of navstate.vertfolder's make_realiases that ignores the
        dummy object. If there was a dummy horz object, the user might be able
        to move back too far. Nope!
        """
        for ch in self.selections:
            ch.make_realiases()

    def add_preset(self, cls, name, preset):
        """
        Add a preset of class `cls` and name `name`. The preset's contents are
        typically a dictionary. However they can be whatever the developer
        pleases tbh.
        """
        if cls not in self.preset_store.keys():
            # Make a new dict if it's not there already.
            self.preset_store[cls] = {}
            self.preset_cmd_store[cls] = {}
        self.preset_store[cls][name] = preset

    def add_preset_cmds(self, cls, name, cmds):
        """
        Add the commands corresponding to preset of class `cls` and name
        `name`. `cmds` is an array with all of the commands needed to execute
        the preset.
        """
        self.preset_cmd_store[cls][name] = cmds

    def get_preset(self, cls, name):
        """
        Return a preset of class `cls` and name `name`. Throws an error if it
        does not exist.
        """
        if cls not in self.preset_store.keys():
            self.error("No such preset class '%s'!" % cls)
        if name not in self.preset_store[cls].keys():
            self.error(
                "No such preset named '%s' of class '%s'!" % 
                (
                    name,
                    cls
                )
            )
        return self.preset_store[cls][name]
    
    def get_preset_cmds(self, cls, name):
        """
        Return the preset commands of class `cls` and name `name`.
        """
        return self.preset_cmd_store[cls][name]
