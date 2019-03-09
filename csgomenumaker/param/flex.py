import random

from ..misc import RANDOM_WORDS

from .param import Param
from .assoc import Assoc
from .paramobj import ParamObj


class Flex(Assoc):
    """
    A special type of param that allows the writer of the config file to
    specify a list of objects by using either a dictionary or list
    construction.
    This class also accepts a few other kwargs which modify its behavior:
    - flexkey
        The key to substitute in for each string value in the list or dict
    - flexkeyname
        The key to substitute in for each string key in the list or dict
    """

    def __init__(self, key, *args, **kwargs):
        Assoc.__init__(self, key, *args, **kwargs)
        self.callback = None

    def evaluate(self, options):
        """
        This overrides Assoc, which overrides ParamObj. Speaking about
        ParamObj's evaluate(), "no, I don't want that!"
        """
        Param.evaluate(self, options)

    def check(self, value):
        """
        Check the given value against the restrictions imposed by this class
        and in kwargs.
        """
        if not isinstance(value, (dict, list)):
            self.type_error((dict, list), type(value))
        out = []
        flexkey = self.default_kwarg("flexkey", "type")
        flexkeyname = self.default_kwarg("flexkeyname", "name")
        if isinstance(value, list):
            # if value is a list, no problemo. We will construct objects as
            # output, using lone strings as `flexkey` and objects as written.
            for el in value:
                if not isinstance(el, (dict, str)):
                    self.type_error_v((dict, str), type(el), el)
                if isinstance(el, str):
                    out.append({flexkey: el})
                elif isinstance(el, dict):
                    out.append(el)
        elif isinstance(value, dict):
            # if value is a dict, no problemo. We will construct objects as
            # output, using lone key/value pairs as `flexkeyname`/`flexkey` and
            # objects as written.
            for el in value:
                k = el
                v = value[el]
                if not isinstance(v, (dict, str)):
                    self.type_error_v((dict, str), type(el), el)
                if isinstance(v, str):
                    out.append({flexkeyname: k, flexkey: v})
                elif isinstance(v, dict):
                    v[flexkeyname] = k
                    out.append(v)
        new = []
        # Callback is for this really weird edge case. Disregard!
        for o in out:
            v = ParamObj.check(self, o)
            if self.callback is not None:
                v = self.callback(o, v)
            new.append(v)
        return new

    def get_example_full(self):
        out = []
        for i in range(0, 3):
            pm = self
            if len(self.children) == 1 and "**object**" in self.children:
                pm = self.children["**object**"]
            out.append(ParamObj.get_example_full(pm))
            out[-1][self.default_kwarg("flexkeyname", "name")] = \
                random.choice(RANDOM_WORDS)
        return out
