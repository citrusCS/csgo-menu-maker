from .command import Command


class Folder(Command):
    """
    Organizes several commands under "one roof".

    Only used for debugging purposes.
    """

    def __init__(self, parent):
        Command.__init__(self, parent, "folder")

    def generate(self):
        return None
