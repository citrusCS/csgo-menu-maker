from .. import misc


class Param(misc.Loggable):
    """
    Represents a single parameter key-value pair in the config.
    """

    def __init__(self, key, *args, **kwargs):
        # Setup - self.key is the key (duh!)
        self.key = key
        self.args = args
        self.kwargs = kwargs

        # Children is a dict with keys being the keys of the value params.
        self.children = {}

        # Mobility -
        self.root = None
        self.parent = None

        # Set if root
        if "root" in self.kwargs:
            if self.kwargs["root"]:
                self.setRoot(self)

        # Value will be set later.
        self.value = None

    def register(self, parent):
        """
        Set the parent and root of each child param. Necessary because they
        have to have some kind of error 'hook' (path) in order to format error
        messages correctly.
        """
        self.parent = parent
        for ch in self.children:
            self.children[ch].register(self)
            self.children[ch].root = self.root

    def evaluate(self, options):
        """
        Try to find and validate the value associated with this instances' key
        (self.key) in the dictionary `options`.
        """
        self.options = options
        if self.key in self.options:
            # We found the key - just make sure it fits
            self.value = self.check(self.options[self.key])
        elif "default" in self.kwargs:
            # We didn't find a key, but that's ok, because there's a default
            self.value = self.kwargs["default"]
        else:
            # We didn't find a key. Bad show.
            self.show_error("Key '%s' not found!" % self.key)

    def check(self, value):
        """
        Validate the given value.

        Overriden by child classes. Some kind of logic (bounds checking, etc.)
        will be applied here.
        """
        return value

    def show_error(self, error):
        """
        Raise an error, but format it so that there is a bit of context given.
        """
        ostring = "%s\n\t... in:\n\t%s" % (error, self.options)
        self.error(ostring)

    def type_error(self, want_type, have_type):
        """
        Raise a type error, meaning that want_type and have_type don't match.
        want_type may be a tuple or list.
        """
        self.type_error_v(want_type, have_type, "key '%s'" % self.key)

    def type_error_v(self, want_type, have_type, v):
        """
        Same as above, but an extra parameter for how to format the key
        specifier. This is useful for printing something with an 'anonymous'
        key, such as a list.
        """
        # Join types like: (int, str) -> "int or str"
        if not isinstance(want_type, tuple):
            want_type = (want_type,)
        need_string = "' or '".join([t.__name__ for t in want_type])
        ostring = "Wrong type for %s! Need '%s', got '%s'." % \
            (
                v,
                need_string,
                have_type.__name__
            )
        self.show_error(ostring)

    def get_error_name(self):
        return (
            self.parent.get_error_name() +
            ".\x1b[1;34m" +
            str(self.key) +
            "\x1b[0m"
        )

    def default_kwarg(self, arg, default):
        """
        Return the value `default` if `arg` was not passed in kwargs, else
        return kwargs[`arg`].
        """
        return default if arg not in self.kwargs else self.kwargs[arg]

    def merge(self, other):
        """
        Merge `other`'s params with `self`'s params. This employs a top-down
        approach, meaning params are only merged if they aren't in this yet.
        """
        for ch in other.children:
            k = ch
            v = other.children[ch]
            if k in self.children:
                if len(v.children):
                    self.children[k].merge(v)
            else:
                self.children[k] = v

    def __str__(self, ilvl=0):
        """
        Return a string representation.
        """
        pre = "\t"*ilvl+self.key+": "
        typ = type(self).__name__
        default = self.kwargs["default"] if "default" in self.kwargs else None
        out = pre+"type=%s,default=%s\n" % (typ, default)
        for k, ch in self.children.items():
            out += ch.__str__(ilvl+1)
        return out

    def get_example(self):
        """
        Generate an example listing(s) from this object only.
        """
        return []

    def get_example_full(self):
        """
        Generate an example listing from this object and possibly its children.
        """
        return {}
