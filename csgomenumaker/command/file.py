from .command import Command


class File(Command):
    """
    Corresponds to a .cfg file with contents. Places each child on a line in
    the file.

    Only used internally by Indirect.
    """

    def __init__(self, parent):
        Command.__init__(self, parent, "file")

        # file_id and bucket correspond to the path location in which the file
        # is placed.
        self.file_id = self.root.get_next_file_id()
        self.bucket = self.file_id % 16

        # text is a list of each line in the file.
        self.text = []

        # Register the file with root so that it knows to create it.
        self.root.file_stash[self.bucket].append(self)

    def __str__(self):
        """
        Wrapper to correctly format the file's path.
        """
        if not self.is_obf:
            if self.name == "":
                return str(self.parent) + "." + self.cls + "-" + str(self.id) \
                    + ".cfg"
            else:
                return str(self.parent) + "." + self.cls + "-" + str(self.id) \
                    + "_" + self.name + ".cfg"
        else:
            # Make the path, e.g. "menumaker/file/6/mm_DEADBEEF.cfg"
            return self.root.name_space + "/file/" + ("%0.1X" % self.bucket) \
                + "/" + self.obf_name + ".cfg"

    def generate(self):
        return "\n".join(self.text)+"\n"
