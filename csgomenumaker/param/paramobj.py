import random

from .param import Param


class ParamObj(Param):
    """
    Takes an arbitrary number of non-keyword arguments through `*args` and
    makes them children parameters - these children parameters are then used to
    evaluate entire objects at once.
    This class also accepts a few other kwargs which modify its behavior:
    - pure
        Raise errors on keys that aren't allowed. Only for debug!
    """

    def __init__(self, *args, **kwargs):
        Param.__init__(self, "**object**", *args, **kwargs)
        for c in self.args:
            self.children[c.key] = c

    def evaluate(self, options):
        """
        Overrides Param.evaluate because default values are not passed to this,
        however we want it to not fail if it doesn't encounter anything either.
        """
        self.options = options
        self.value = self.check(self.options)

    def check(self, value):
        """
        Check the given value against the restrictions imposed by this class
        and in kwargs.
        """
        if not isinstance(value, dict):
            self.type_error(dict, type(value))
        pure = self.default_kwarg("pure", False)
        out = value
        for v in value:
            if pure:
                if v not in self.children:
                    self.show_error("Found unallowed key '%s'." % v)
        # Evaluate children and construct an array with their outputs.
        for v in self.children:
            self.children[v].evaluate(value)
            out[v] = self.children[v].value
        return out

    def __getitem__(self, key):
        """
        Convenience method for easy access.
        """
        return self.value[key]

    def get_example_full(self):
        """
        Generate an example listing from this object and its children.
        """
        out = {}
        for k, p in self.children.items():
            if "nodoc" in p.kwargs and p.kwargs["nodoc"]:
                continue
            if "default" in p.kwargs:
                out[k] = p.kwargs["default"]
            elif "ex_vals" in p.kwargs:
                out[k] = random.choice(p.kwargs["ex_vals"])
            else:
                out[k] = p.get_example_full()
        return out
