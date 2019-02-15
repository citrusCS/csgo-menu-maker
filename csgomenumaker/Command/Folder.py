from .Command import Command


class Folder(Command):
    def __init__(self, parent):
        Command.__init__(self, parent, "folder")

    def generate(self):
        return None
