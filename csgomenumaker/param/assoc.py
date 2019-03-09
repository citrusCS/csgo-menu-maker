from .param import Param
from .paramobj import ParamObj


class Assoc(ParamObj):
    """
    A version of ParamObj which allows a key as an argument, for use with sub-
    objects.
    """

    def __init__(self, key, *args, **kwargs):
        Param.__init__(self, key, *args, **kwargs)
        for c in self.args:
            self.children[c.key] = c
