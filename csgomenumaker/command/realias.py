from .command import Command


class Realias(Command):
    """
    Aliases a command to another command at runtime (when its alias is called.)
    
    Used to rebind Null to Placeholder and vice versa.
    """
    def __init__(self, parent, dest, src):
        Command.__init__(self, parent, "realias")
        
        # dest is the command that will get overwritten, src is the command to
        # copy from
        self.dest = dest
        self.src = src
        
        # This command is not a collection, and has no unwanted side-effects.
        self.clean = True

    def generate(self):
        #if self.dest is self.root.globals["void"]:
        #    print(self)
        return "alias " + str(self.dest) + " " + str(self.src)
