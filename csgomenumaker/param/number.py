import random

from ..misc.math import *

from .param import Param

class Number(Param):
    """
    A param type which accepts only a number. 
    This class also accepts a few other kwargs which modify its behavior:
    - choices
        Only allow integers in this list.
    - int
        Only allow integers for this parameter.
    - min
        Only allow values higher than this.
    - max
        Only allow values lower than this.
    """
    def check(self, value):
        """
        Check the given value against the restrictions imposed by this class
        and in kwargs.
        """
        if not isinstance(value, (int, float)):
            self.type_error((int,), type(value))
        if "choices" in self.kwargs:
            choices = self.kwargs["choices"]
            if value not in choices:
                orstr = " or ".join(["'%s'" % ch for ch in choices])
                self.show_error(("Value not acceptable for key '%s'! " %
                        (
                            self.key
                        )
                    ) +
                    (
                        "Accepted values are %s." %
                        (
                            orstr
                        )
                    )
                )   
        if "int" in self.kwargs and self.kwargs["int"]:
            if not isinstance(value, int):
                if not value.is_integer():
                    self.show_error(
                        "Value for key '%s' is not an integer! ('%f')" %
                        (
                            self.key,
                            value
                        )
                    )
        if "min" in self.kwargs:
            if value < self.kwargs["min"]:
                self.show_error("Value too low for key '%s' (%f < %f)!" %
                    (
                        self.key,
                        value,
                        self.kwargs["min"]
                    )
                )
        if "max" in self.kwargs:
            if value > self.kwargs["max"]:
                self.show_error("Value too high for key '%s' (%f > %f)!" %
                    (
                        self.key,
                        value,
                        self.kwargs["max"]
                    )
                )
        return value
    
    def get_example(self):
        """
        Get an example set of values for this object, taking into account
        kwarg restrictions.
        """
        out = []
        if "choices" in self.kwargs:
            out.append((1234, False, "Not in list of allowed choices."))
            out.append((choices[0], True, "In list of allowed choices."))
            if len(choices) > 1:
                out.append((choices[1], True, "In list of allowed choices."))
        if "max" in self.kwargs:
            min = max-10 if "min" not in self.kwargs else self.kwargs["min"]
            max = self.kwargs["max"]
            vno = max+10
            rnd = 2 if "int" not in self.kwargs else 2 if not \
                self.kwargs["int"] else 0
            vyes = round(lerp(min, max, 0.8), rnd)
            out.append(
                (
                    vno,
                    False,
                    "Value too large for maximum (%f > %f)" % (vno, max)
                )
            )
            out.append(
                (
                    vyes,
                    True,
                    "Value is less than maximum (%f < %f)" % (vyes, max)
                )
            )
        if "min" in self.kwargs:
            min = self.kwargs["min"]
            max = min+10 if "max" not in self.kwargs else self.kwargs["max"]
            vno = min-10
            rnd = 2 if "int" not in self.kwargs else 2 if not \
                self.kwargs["int"] else 0
            vyes = round(lerp(min, max, 0.2), rnd)
            out.append(
                (
                    vno,
                    False,
                    "Value too small for minimum (%f < %f)" % (vno, min)
                )
            )
            out.append(
                (
                    vyes,
                    True,
                    "Value is greater than minimum (%f <>%f)" % (vyes, min)
                )
            )
        if "int" in self.kwargs:
            min = 0 if "min" not in self.kwargs else self.kwargs["min"]
            max = 0 if "max" not in self.kwargs else self.kwargs["max"]
            out.append(
                (
                    lerp(min, max, 0.8)+0.1234,
                    False,
                    "Value has a fractional component."
                )
            )
            out.append(
                (
                    round(lerp(min, max, 0.8)),
                    True,
                    "Value is an integer."
                )
            )
    
    def get_example_full(self):
        """
        Get a single valid example value for this parameter.
        """
        if "choices" in self.kwargs:
            return random.choice(self.kwargs["choices"])
        else:
            val = round(random.uniform(0, 10), 2)
            if "min" in self.kwargs and "max" in self.kwargs:
                val = lerp(
                    self.kwargs["min"],
                    self.kwargs["max"],
                    random.uniform(0, 1)
                )
            elif "min" in self.kwargs:
                val = lerp(
                    self.kwargs["min"],
                    self.kwargs["min"] + 10,
                    random.uniform(0, 1)
                )
            elif "max" in self.kwargs:
                val = lerp(
                    self.kwargs["max"] - 10,
                    self.kwargs["max"],
                    random.uniform(0, 1)
                )
            if "int" in self.kwargs and self.kwargs["int"]:
                val = round(val)
            else:
                val = round(val, 2)
            return val