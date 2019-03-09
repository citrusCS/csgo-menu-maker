import copy
import sys

from .. import command
from .. import misc
from .. import param


class Menu(command.navstate.Vert, misc.Loggable):
    """
    A UI menu object.

    This is an intermediate class between command.navstate and Component
    classes. It handles things like parameters, error printing, and primitive
    command management.

    All components, one way or another, inherit from this.
    """
    params = param.ParamObj(
        param.Name("Generic Menu"),
        param.Desc("Description Here")
    )

    def __init__(self, parent, options):
        command.navstate.Vert.__init__(self, parent)
        self.cls = "menu"

        # Figure out the root object. Could use a bit of optimization.
        self.menu_root = self
        if not hasattr(self, "is_menu_root"):
            self.is_menu_root = False
        while not self.menu_root.is_menu_root:
            self.menu_root = self.menu_root.parent

        # Try to obtain the component's name early, for error logging.
        if "name" in self.params.children:
            self.ui_name = self.params.children["name"].kwargs["default"]

        # Merge+evaluate params. Then, set the name and description.
        self.merge_params()

        if not self.root.example or self.is_menu_root:
            self.options = options
        else:
            self.options = self.params.get_example_full()

        self.params.evaluate(self.options)
        self.ui_name = self.params["name"]
        self.desc = self.params["desc"]

    def get_params(self, cur_type):
        """
        Return the params associated with this object.

        Called as merge_params walks up the class inheritance chain until it
        hits Menu. This function is overrideable, but is a bit of a pain.
        """
        # Since we're using an attribute from a type object, we must copy as
        # Param retains certain state. Could use optimzation in Param so that
        # it can evaluate multiple times.
        newpars = copy.deepcopy(cur_type.params)
        newpars.register(self)
        return (newpars, cur_type.__base__)

    def merge_params(self):
        """
        Merge down type params, starting from the most child-like class.

        This is done by walking up the class hierarchy and merging at each
        step.
        """
        # Overwrite self.params temporarily
        self.params = param.ParamObj()
        self.params.register(self)

        # cur_type holds the currently inspected type, that is, where we are
        # getting params from.
        cur_type = type(self)
        while cur_type is not Menu.__base__:
            # If the type defines its own parameters, we use them. Otherwise,
            # move on.
            if hasattr(cur_type, "params"):
                # gpfunc is cur_type's version of get_params. Remember, it is
                # overrideable.
                gp_func = cur_type.get_params
                newpars, next_type = gp_func(self, cur_type)
                self.params.merge(newpars)
                cur_type = next_type
            else:
                cur_type = cur_type.__base__

    def make_cmd(self, cmd, value):
        """
        Convenience function to make a concmd/convar statement out of a command
        (or convar) and a value (which can be int, float, or str).

        Returns a command.Primitive.
        """
        if isinstance(value, int):
            return command.Primitive(self, cmd, "%i" % value)
        elif isinstance(value, float):
            return command.Primitive(self, cmd, "%f" % value)
        elif isinstance(value, str):
            return command.Primitive(self, cmd, "%s" % value)
