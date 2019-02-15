from .Command import Command
from .Primitive import Primitive


class Echo(Primitive):
    def __init__(self, parent, text, out=False):
        Primitive.__init__(self, parent, "echo", [])
        self.cls = "primitive-echo"
        if not out:
            self.text = self.root.filterChar+self.root.filterAfter+text
        else:
            self.text = self.root.filterCharOut+self.root.filterAfter+text
        self.setClean(False)
        self.addArg('"'+self.text+'"')

    def generate(self):
        return Primitive.generate(self)
