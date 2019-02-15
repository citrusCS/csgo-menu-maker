import sys

from .. import Command


class Menu(Command.NavState.Vert):
    def __init__(self, parent, options):
        Command.NavState.Vert.__init__(self, parent)
        if not hasattr(self, "isMenuRoot"):
            self.isMenuRoot = False
        self.cls = "menu"
        self.options = options
        self.menuRoot = self
        while not self.menuRoot.isMenuRoot:
            self.menuRoot = self.menuRoot.parent
        self.setSpecs()

    def setSpecs(self):
        if hasattr(self, "defaultName"):
            self.setUIName(
                self.optValue(
                    self.options,
                    "name",
                    self.defaultName
                )
            )
            self.setDesc(
                self.optValue(
                    self.options,
                    "desc",
                    self.defaultDesc
                )
            )

    def compareType(self, t1, t2):
        if t2 == int:
            t2 = type(float())
        if t1 == int:
            t1 = type(float())
        return t1 == t2

    def optValue(self, obj, key, default=None):
        keyPresent = False
        if isinstance(obj, list):
            keyPresent = key < len(obj)
        else:
            keyPresent = key in obj
        if keyPresent:
            val = obj[key]
            if self.compareType(type(val), type(default)):
                return obj[key]
            else:
                self.error(
                    (
                        "Mismatched type for key '%s' on object '%s', "
                        + "expected '%s', got '%s'"
                    ) %
                    (
                        key,
                        obj,
                        type(default),
                        type(obj)
                    )
                )
        else:
            if default is not None:
                return default
            else:
                self.error("Expected key '%s' in object '%s'" % (key, obj))

    def optTypeKey(self, obj, key, typeTemplate):
        if key in obj:
            if not self.compareType(type(obj[key]), type(typeTemplate)):
                self.error(
                    "Mismatched type for key '%s' on object '%s', "
                    + "expected '%s', got '%s'" %
                    (
                        key,
                        obj,
                        type(typeTemplate),
                        type(obj)
                    )
                )
        else:
            self.error("Expected key '%s' in object '%s'" % (key, obj))

    def optType(self, obj, typeTemplate):
        if type(obj) != type(typeTemplate):
            self.error(
                "Mismatched type for object '%s', "
                + "expected '%s', got '%s'" %
                (
                    obj,
                    type(typeTemplate),
                    type(obj)
                )
            )

    def optLenZero(self, obj):
        if len(obj) == 0:
            self.error("Not enough elements in object '%s', (need >0)" % obj)

    def optLenZeroName(self, objn, obj):
        if len(obj) == 0:
            self.error("Not enough elements in object '%s', (need >0)" % objn)

    def makeCmd(self, cmd, value):
        if isinstance(value, int):
            return Command.Primitive(self, cmd, "%i" % value)
        elif isinstance(value, float):
            return Command.Primitive(self, cmd, "%f" % value)
        elif isinstance(value, str):
            return Command.Primitive(self, cmd, "%s" % value)

    def makeCmdList(self, cmdList):
        comp = Command.Compound(self)
        for cmd in cmdList:
            self.optType(cmd, str())
            spl = cmd.split(" ")
            self.optLenZero(spl)
            concmd, ag = (spl[0], spl[1:])
            Command.Primitive(comp, concmd, ag)
        return comp

    def error(self, s):
        print("%s:\n\t\x1b[31mError: %s\x1b[0m" % (self.getErrorName(), s))
        sys.exit(1)
