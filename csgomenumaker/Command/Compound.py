from .command import Command, \
    COMMAND_EVAL_REGISTER, COMMAND_EVAL_NONE, COMMAND_EVAL_COMBINE


class Compound(Command):
    """
    A collection of multiple Commands.
    
    Resolves to an alias command with multiple chained commands separated by
    statement separators in the Source console (by default, ';'). The chained
    commands are the commands located in the `children` attribute.
    
    Used as an abstraction to make multiple commands run under one command's
    accord.
    """
    def __init__(self, parent):
        Command.__init__(self, parent, "compound")

    def generate(self):
        output = ""
        
        # Loop through children and add evaluate each one, but cut corners
        # along the way.
        for cmd in self.children:
            # Space can be conserved if we are smart about generating these.
            # If a command has no references (it is 'clean'), then its
            # generated form can be immediately substituted in instead of a
            # reference. Note that if it has already been evaluated, it cannot
            # be optimized in this way.
            if cmd.clean and cmd.eval_state == COMMAND_EVAL_REGISTER:
                gen = cmd.generate()
                
                # The max command length for commands is 1024 characters. We
                # play it safe here (only 1000, in reality about 1014-1015 with 
                # overhead)
                if len(gen) + len(output) < 1000:
                    output += cmd.generate()+";"
                    cmd.eval = COMMAND_EVAL_COMBINE
                else:
                    output += cmd+";"
            else:
                output += cmd+";"
        return output
