import random

from ..misc import RANDOM_WORDS

from .param import Param
from .number import Number


class Sequence(Param):
    """
    A list of objects.
    This class also accepts a few other kwargs which modify its behavior:
    - seqlen
        Raise an error if the input value is not this length.
    - seqtypes
        Check each object in the input value against this tuple of types.
    - zerook
        Don't raise an error if there are zero elements. 'Sall good!
    - number
        Check each value with Number.check() as well, with other kwargs
        pertaining to Number.
    """

    def __init__(self, key, *args, **kwargs):
        Param.__init__(self, key, *args, **kwargs)
        if "seqtypes" in self.kwargs:
            if not isinstance(self.kwargs["seqtypes"], tuple):
                self.kwargs["seqtypes"] = (self.kwargs["seqtypes"],)

    def check(self, value):
        """
        Check the given value against the restrictions imposed by this class
        and in kwargs.
        """
        if not isinstance(value, list):
            self.type_error(list, type(value))
        if "seqlen" in self.kwargs:
            if self.kwargs["seqlen"] != len(value):
                self.show_error(
                    (
                        "Length out of range for key '%s' ('%s')! " %
                        (
                            self.key,
                            value
                        )
                    ) +
                    (
                        "(%i != %i)" %
                        (
                            len(value),
                            self.kwargs["seqlen"]
                        )
                    )
                )
        if "seqtypes" in self.kwargs:
            for i, v in enumerate(value):
                if not isinstance(v, self.kwargs["seqtypes"]):
                    self.type_error_v(
                        (float, int),
                        type(v),
                        "object %i" % i
                    )
        if "number" in self.kwargs and self.kwargs["number"]:
            temp_key = self.key
            for i, v in enumerate(value):
                self.key = "element '%i' of key '%s'" % (i, temp_key)
                value[i] = Number.check(self, value[i])
        zerook = self.default_kwarg("zerook", False)
        if not zerook:
            if not len(value):
                self.show_error(
                    (
                        "Length out of range for key '%s' ('%s')! " %
                        (
                            self.key,
                            value
                        )
                    ) +
                    (
                        "(%i == %i)" %
                        (
                            len(value),
                            0
                        )
                    )
                )
        return value

    def get_example_val(self, rtype=True):
        """
        Return one (1) value which represents an allowed list value.
        """
        if "seqtypes" in self.kwargs:
            templ = random.choice(self.kwargs["seqtypes"])
            if templ == str:
                return random.choice(RANDOM_WORDS)
            elif templ == float or templ == int:
                if "number" in self.kwargs and self.kwargs["number"]:
                    return Number.get_example_full(self)
                else:
                    return random.randint(0, 10)
        if "number" in self.kwargs:
            return Number.get_example_full(self)

    def get_example(self):
        """
        Get an example set of values for this object, taking into account
        kwarg restrictions.
        """
        out = []
        ex_amt = 3 if "seqlen" not in self.kwargs else \
            self.kwargs["seqlen"]
        if "seqlen" in self.kwargs:
            exlist = []
            for i in range(0, self.kwargs["seqlen"]-1):
                exlist.append(self.get_example_val())
            out.append(
                exlist,
                False,
                "Invalid number of elements in sequence (%i != %i)" % (
                    self.kwargs["seqlen"]-1,
                    self.kwargs["seqlen"]
                )
            )
            exlist = []
            for i in range(0, self.kwargs["seqlen"]):
                exlist.append(self.get_example_val())
            out.append(
                exlist,
                False,
                "Correct number of elements in sequence (%i == %i)" % (
                    self.kwargs["seqlen"],
                    self.kwargs["seqlen"]
                )
            )
        if "seqtypes" in self.kwargs:
            exlist = []
            if str not in self.kwargs["seqtypes"]:
                for i in range(0, ex_amt):
                    exlist.append(random.choice(RANDOM_WORDS))
            elif int not in self.kwargs["seqtypes"]:
                for i in range(0, ex_amt):
                    exlist.append(random.randint(0, 10))
            out.append(
                exlist,
                False,
                "Incorrect type for sequence elements."
            )
            exlist = []
            for i in range(0, ex_amt):
                exlist.append(self.get_example_val())
            out.append(
                exlist,
                True,
                "Correct type for sequence elements."
            )
        if "zerook" in self.kwargs:
            vnot = True
            if self.kwargs["zerook"]:
                vnot = False
            exlist = []
            out.append(
                exlist,
                not vnot,
                "Cannot have length of zero!"
            )
            exlist = []
            for i in range(0, ex_amt):
                exlist.append(self.get_example_val())
            out.append(
                exlist,
                vnot,
                "More than zero elements in this sequence."
            )
        return out

    def get_example_full(self):
        """
        Get a single valid example value for this parameter.
        """
        out = []
        ex_amt = 3 if "seqlen" not in self.kwargs else \
            self.kwargs["seqlen"]
        for i in range(0, ex_amt):
            out.append(self.get_example_val())
        return out
