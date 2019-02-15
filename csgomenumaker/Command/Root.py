import os

from .Command import Command, COMMAND_EVAL_REGISTER, COMMAND_EVAL_NONE
from .Null import Null


class Root(Command):
    def __init__(self):
        self.root = self
        self.idCtr = -1
        self.fileIdCtr = -1
        Command.__init__(self, self, "root")
        self.children = []
        self.globals = {}
        self.registry = []
        self.binds = {}
        self.obf = True
        self.config = None
        self.echoCache = {}
        # R = 1 | D = 2 | L = 4 | U = 8
        self.boxDrawing = [
            "\u0020",   "\u2576",   "\u2577",   "\u250C",
            "\u2574",   "\u2500",   "\u2510",   "\u252C",
            "\u2575",   "\u2514",   "\u2502",   "\u251C",
            "\u2518",   "\u2534",   "\u2524",   "\u253C"
        ]
        self.filterChar = "\u03BB"
        self.filterCharOut = "\u0394"
        self.filterAfter = " | "
        self.blockChar = "\u2588"
        self.padChar = "."
        self.fileStash = [[] for _ in range(16)]
        self.nameSpace = "menumaker"
        self.namePrefix = "mm"
        self.classMapping = {}
        self.startup = None

    def __str__(self):
        return self.namePrefix

    def getId(self):
        self.idCtr += 1
        return self.idCtr

    def getFileId(self):
        self.fileIdCtr += 1
        return self.fileIdCtr

    def getGlobal(self, name):
        return self.globals[name]

    def addGlobal(self, name, ref):
        self.globals[name] = ref

    def addBind(self, key, ref):
        self.binds[key] = ref

    def makeAll(self):
        self.register()
        self.out = ""
        self.startupTemp = Null(self)
        if self.obf:
            mapping = ""
            for c in self.registry:
                if c.isobf:
                    continue
                pname = str(c)
                if c.statePrefix == "+":
                    other = c.statePrefixOther
                    other.setOName("-%s_%0.8X" % (self.namePrefix, c.id))
                nname = "%s%s_%0.8X" % (c.statePrefix, self.namePrefix, c.id)
                c.setOName(nname)
        self.out += self.combine()
        for k in self.binds.keys():
            self.out += "bind \"%s\" \"%s\"\n" % (k, str(self.binds[k]))
        self.out += self.startup.generate()+"\n"
        os.makedirs(self.nameSpace, exist_ok=True)
        os.makedirs(self.nameSpace+"/file", exist_ok=True)
        maincfg = open(self.nameSpace+"/main.cfg", "wb")
        maincfg.write(self.out.encode("utf-8"))
        maincfg.close()
        for i, fs in enumerate(self.fileStash):
            os.makedirs(self.nameSpace + "/file/%0.1X" % i, exist_ok=True)
            for fc in fs:
                fcfg = open(self.nameSpace + "/file/%0.1X/%s.cfg"
                            % (i, fc.getNameReal()), "wb")
                fcfg.write(fc.generate().encode("utf-8"))
                fcfg.close()

    def register(self):
        self.eval = COMMAND_EVAL_REGISTER
        for ch in self.children:
            if ch.eval == COMMAND_EVAL_NONE:
                ch.register()

    def addFile(self, ref, bucket):
        self.fileStash[bucket].append(ref)

    def addClass(self, name, tp):
        self.classMapping[name] = tp

    def getClass(self, name):
        return self.classMapping[name]

    def getErrorName(self):
        return self.namePrefix

    def setStartup(self, ref):
        self.startup = ref

    def setConfig(self, config):
        self.config = config
