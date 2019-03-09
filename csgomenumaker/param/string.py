import random

from ..misc import RANDOM_WORDS

from .param import Param


class String(Param):
    """
    A param type which only accepts a string.
    This class also accepts a few other kwargs which modify its behavior:
    - choices
        Only allow strings in this list.
    """

    def check(self, value):
        """
        Check the given value against the restrictions imposed by this class
        and in kwargs.
        """
        if "default" in self.kwargs and value == self.kwargs["default"]:
            return value
        if not isinstance(value, str):
            self.type_error((str,), type(value))
        if "choices" in self.kwargs:
            if value not in self.kwargs["choices"]:
                self.show_error(
                    "Value '%s' not in set of choices '%s'." %
                    (
                        value,
                        str(self.kwargs["choices"])
                    )
                )
        return value

    def get_example(self):
        """
        Get an example set of values for this object, taking into account
        kwarg restrictions.
        """
        out = []
        out.append(
            (
                1234.5678,
                False,
                "Value is not a string."
            )
        )
        if "choices" in self.kwargs and self.kwargs["choices"]:
            out.append(
                (
                    random.choice(self.kwargs["choices"]),
                    True,
                    "Value is a string."
                )
            )
            out.append(
                (
                    random.choice(RANDOM_WORDS),
                    False,
                    "Value is not an allowed choice."
                )
            )
            out.append(
                (
                    random.choice(self.kwargs["choices"]),
                    True,
                    "Value is an allowed choice."
                )
            )
        else:
            out.append(
                (
                    random.choice(RANDOM_WORDS),
                    True,
                    "Value is a string."
                )
            )
        return out

    def get_example_full(self):
        """
        Get a single valid example value for this parameter.
        """
        if "choices" in self.kwargs and self.kwargs["choices"]:
            return random.choice(self.kwargs["choices"])
        else:
            return random.choice(RANDOM_WORDS)
