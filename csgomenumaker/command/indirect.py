from .command import Command
from .file import File


class Indirect(Command):
    """
    Wrapper around File to correctly generate exec commands.
    
    This should be used if you need to make a file with command contents.
    """
    def __init__(self, parent):
        Command.__init__(self, parent, "indirect")
        
        # Container is not really a container. I shouldn't have named it that.
        self.container = File(self)
        
        # Set the hide_children flag, as this command's contents should not be
        # put into `main.cfg`.
        self.hide_children = True

    def generate(self):
        # Loop through children and generate them, putting their outputs into
        # the container. Note that each child must not reference another cmd.
        # Thus, all commands in this should really be Primitives or aliases to
        # commands that contain no circular references.
        for cmd in self.children:
            if cmd == self.container:
                continue
            line = cmd.generate()
            self.container.text.append(line)
        return "exec " + str(self.container)
