COMMAND_EVAL_NONE = 0
COMMAND_EVAL_REGISTER = 1
COMMAND_EVAL_COMBINE = 2


class Command:
    def __init__(self, parent, cls):
        self.parent = parent
        self.root = self.parent.root
        self.cls = cls
        self.id = self.root.getId()
        self.name = ""
        self.oname = None
        self.isobf = False
        self.children = []
        self.eval = COMMAND_EVAL_NONE
        self.clean = False
        self.hideChildren = False
        self.parent.children.append(self)
        self.statePrefix = ""
        self.statePrefixOther = None

    def __str__(self):
        if not self.isobf:
            if self.name == "":
                return str(self.parent) + "." + self.cls + "-" + str(self.id)
            else:
                return str(self.parent) + "." + self.cls + "-" + str(self.id) \
                        + "_" + self.name
        else:
            return self.oname

    def __add__(self, other):
        if type(other) == str:
            return str(self) + other
        return None

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def addChild(self, ref):
        self.children.append(ref)

    def setName(self, name):
        self.name = name

    def setOName(self, name):
        self.oname = name
        self.isobf = True

    def getNameReal(self):
        if self.isobf:
            return self.oname
        else:
            return self.name

    def register(self):
        self.eval = COMMAND_EVAL_REGISTER
        for ch in self.children:
            if ch.eval == COMMAND_EVAL_NONE:
                ch.register()
        self.root.registry.append(self)

    def combine(self):
        self.eval = COMMAND_EVAL_COMBINE
        self.out = ""
        for ch in self.children:
            if ch.eval == COMMAND_EVAL_REGISTER:
                gen = ch.generate()
                if gen is not None:
                    self.out += "alias \""+str(ch)+"\" \""+gen+"\"\n"
                self.out += ch.combine()
        if self.hideChildren:
            return ""
        else:
            return self.out

    def generate(self):
        return ""

    def addGlobal(self, name):
        self += self.root.getGlobal(name)

    def getErrorName(self):
        if hasattr(self, "getUIName"):
            return self.parent.getErrorName()+"."+self.getUIName()
        else:
            if self.name == "":
                return self.parent.getErrorName() + "." + self.cls + "-" \
                        + str(self.id)
            else:
                return self.parent.getErrorName() + "." + self.cls + "_" \
                        + self.name

    def setClean(self, clean):
        self.clean = clean
