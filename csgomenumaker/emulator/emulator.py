from .. import misc

class Emulator(misc.Loggable):
    """
    Console emulator. Used for testing.
    """
    def __init__(self):
        self.lastcmd = []
        self.commands = {}
        self.aliases = {}
        self.binds = {}

    def tokenize_line(self, line):
        """
        Split a line into a list of lists such that the outer list is a list of
        all separate commands in a line, and the inner list is the arguments to
        those commands. This works very similarly to how CS:GO's actual
        tokenization process works:
        https://github.com/id-Software/Quake/blob/master/WinQuake/cmd.c
        """
        cmds = []
        curcmd = []
        curarg = ""
        isquoted = False
        for i, c in enumerate(line):
            # If this isn't in a quote
            if not isquoted:
                if c in " \t":
                    # Ignore whitespace
                    if len(curarg):
                        curcmd.append(curarg)
                    curarg = ""
                elif c == '"':
                    isquoted = True
                    curarg = ""
                elif c == ';':
                    # Split into another command
                    if len(curarg):
                        curcmd.append(curarg)
                    if len(curcmd):
                        cmds.append(curcmd)
                    curcmd = []
                    curarg = ""
                elif c == '\n':
                    pass
                else:
                    curarg += c
            else:
                if c == '"':
                    isquoted = False
                    curcmd.append(curarg)
                    curarg = ""
                elif c == '\n':
                    self.error("Expected end of quote at character %i!" % i)
                else:
                    curarg += c
            if i > 1000:
                self.error("Command too long! (%i > 1000)" % i)
        if len(curarg):
            curcmd.append(curarg)
        if len(curcmd):
            cmds.append(curcmd)
        return cmds
    
    def evaluate_cmds(self, cmds):
        """
        Evaluate a tokenized set of commands and arguments.
        """
        for cmd in cmds:
            if len(cmd) == 0:
                self.error("Not enough arguments for command %s!" % cmd)
                return
            if cmd[0] == "alias":
                if self.cmd_args(cmd, 3):
                    return
                dest = cmd[1]
                src = cmd[2]
                self.aliases[dest] = src
                print("[ALIAS] %s <- %s" % (dest, src))
            elif cmd[0] == "echo":
                print("[ECHO] %s" % " ".join(cmd[1:] if len(cmd) > 1 else ""))
            elif cmd[0] == "exec":
                if self.cmd_args(cmd, 2):
                    return
                print("[EXEC] %s" % cmd[1])
                f = None
                try:
                    f = open(cmd[1], 'r')
                except:
                    self.error("Couldn't open file %s!" % cmd[1])
                    return
                l = f.readlines()
                #print(l)
                f.close()
                for line in l:
                    tok = self.tokenize_line(line)
                    self.evaluate_cmds(tok)
            elif cmd[0] == "bind":
                if self.cmd_args(cmd, 3):
                    return
                print("[BIND] %s -> %s" % (cmd[1], cmd[2]))
                self.binds[cmd[1]] = cmd[2]
            elif cmd[0] == "unbind":
                if self.cmd_args(cmd, 2):
                    return
                print("[UNBIND] %s" % cmd[1])
                self.binds.pop(cmd[1], None)
            elif cmd[0] == "trigger" or cmd[0] == "t":
                if self.cmd_args(cmd, (2,3)):
                    return
                amt = 1
                if cmd[1] not in self.binds:
                    self.error("Key %s not bound!" % cmd[1])
                    return
                if len(cmd) == 3:
                    amt = int(cmd[2])
                print("[TRIGGER] %s" % cmd[1])
                for _ in range(amt):
                    tok = self.tokenize_line(self.binds[cmd[1]])
                    self.evaluate_cmds(tok)
            elif cmd[0] == "'":
                self.evaluate_cmds(self.lastcmd)
            else:
                # Command not found, assume it's ok
                if cmd[0] in self.aliases:
                    tok = self.tokenize_line(self.aliases[cmd[0]])
                    self.evaluate_cmds(tok)
                else:
                    print("[RUN] \"%s\"" % " ".join(cmd))
            if cmd[0] != "'":
                self.lastcmd = cmds
    
    def cmd_args(self, cmd, args):
        """
        Check if arguments are in range, or equal to args, which can be a 
        single number or a tuple range.
        """
        if isinstance(args, int):
            if len(cmd) == args:
                return 0
            else:
                self.error(
                    "Expected %i arguments for command '%s', but got %i." %
                    (
                        args,
                        " ".join(cmd),
                        len(cmd)
                    )
                )
                return 1
        elif isinstance(args, tuple):
            if len(cmd) in range(args[0], args[1]+1):
                return 0
            else:
                self.error(
                    "Expected %i-%i arguments for command '%s', but got %i." %
                    (
                        args[0],
                        args[1],
                        " ".join(cmd),
                        len(cmd)
                    )
                )
                return 1
    
    def repl(self):
        """
        Run an input loop.
        """
        while True:
            inp = input("\x1b[34m] ")
            print("\x1b[0m",end="")
            tok = self.tokenize_line(inp)
            self.evaluate_cmds(tok)
    
    def error(self, text):
        misc.Loggable.error(self, text, exit=False)