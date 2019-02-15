from .Command import Command


class File(Command):
    def __init__(self, parent):
        Command.__init__(self, parent, "file")
        self.fileId = self.root.getFileId()
        self.bucket = self.fileId % 16
        self.text = []
        self.root.addFile(self, self.bucket)

    def __str__(self):
        if not self.isobf:
            if self.name == "":
                return str(self.parent) + "." + self.cls + "-" + str(self.id) \
                    + ".cfg"
            else:
                return str(self.parent) + "." + self.cls + "-" + str(self.id) \
                    + "_" + self.name + ".cfg"
        else:
            return self.root.nameSpace + "/file/" + ("%0.1X" % self.bucket) \
                + "/" + self.oname + ".cfg"

    def addLine(self, line):
        self.text.append(line)

    def generate(self):
        return "\n".join(self.text)+"\n"
