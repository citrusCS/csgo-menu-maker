from .Command import Command, \
    COMMAND_EVAL_REGISTER, COMMAND_EVAL_NONE, COMMAND_EVAL_COMBINE


class Compound(Command):
    def __init__(self, parent):
        Command.__init__(self, parent, "compound")

    def generate(self):
        out = ""
        for cmd in self.children:
            if cmd.clean and cmd.eval == COMMAND_EVAL_REGISTER:
                gen = cmd.generate()
                if len(gen) + len(out) < 1000:
                    out += cmd.generate()+";"
                    cmd.eval = COMMAND_EVAL_COMBINE
                else:
                    out += cmd+";"
            else:
                out += cmd+";"
        return out
