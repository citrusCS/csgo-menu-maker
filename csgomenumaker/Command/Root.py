import os

from .command import *


class Root(Command):
    """
    The root command object.
    """
    def __init__(self):
        # Set these so that we don't go into an infinite loop or some shit.
        self.root = self
        self.id_ctr = -1
        self.file_id_ctr = -1
        
        Command.__init__(self, self, "root")
        
        # Info caches which will be used by children and for generating files.
        self.children = []
        self.globals = {}
        self.registry = []
        self.binds = {}
        self.file_stash = [[] for _ in range(16)]
        self.class_mapping = {}
        
        self.do_obf = True
        self.config = None
        self.startup = None
        
        # Formatting specifics.
        # R = 1 | D = 2 | L = 4 | U = 8
        self.box_drawing = [
            "\u0020",   "\u2576",   "\u2577",   "\u250C",
            "\u2574",   "\u2500",   "\u2510",   "\u252C",
            "\u2575",   "\u2514",   "\u2502",   "\u251C",
            "\u2518",   "\u2534",   "\u2524",   "\u253C"
        ]
        self.filter_char = "\u03BB"
        self.filter_char_out = "\u0394"
        self.filter_after = " | "
        self.block_char = "\u2588"
        self.pad_char = "."
        self.name_space = "menumaker"
        self.name_prefix = "mm"

    def __str__(self):
        """
        Overrides Command.__str__() so that an infinite loop is avoided.
        """
        return self.name_prefix

    def get_next_id(self):
        """
        Get a unique id suitable for use in a new command.
        """
        self.id_ctr += 1
        return self.id_ctr

    def get_next_file_id(self):
        """
        Get a unique id suitable for use in a .cfg filename.
        """
        self.file_id_ctr += 1
        return self.file_id_ctr

    def make_all(self):
        """
        Generate EVERYTHING.
        
        Register commands, generate commands, generate binds, and write .cfgs.
        """
        # 1. Register all commands (add to self.registry)
        self.register()
        
        # 2. Obfuscate (mangle) all names. This is similar to how C++ compilers
        #    do it. I need to do this because aliases (cmdalias_t, if you're
        #    into the source code) can only have a maximum name length of 32
        #    characters. As long as there aren't more than 2^32 commands, there
        #    should be no problems.
        if self.do_obf:
            mapping = ""
            for c in self.registry:
                # Only obfuscate names that haven't been yet.
                if c.is_obf:
                    continue
                # Generate state prefixes a la (+forward, -forward)
                if c.state_prefix == "+":
                    other = c.state_prefix_other
                    other.is_obf = True
                    other.obf_name = nname
                # Format like: "mm_XXXXXXXX"
                nname = "%s%s_%0.8X" % (c.state_prefix, self.name_prefix, c.id)
                c.is_obf = True
                c.obf_name = nname
        
        # 3. Generate all of the commands. This is done by a single call to the
        #    RECURSIVE function combine(), which generates all of its children.
        #    It returns a string which is essentially most of main.cfg.
        out = self.combine()
        
        # 4. Generate all binds. Bind all keys to their function, usually a
        #    void command that will get overwritten by the UI engine.
        for k in self.binds.keys():
            out.append('bind "%s" "%s"' % (k, str(self.binds[k])))
            
        # 5. Generate the startup command. This is the entry point to the whole
        #    engine. It's the only statement in the file that isn't a bind or
        #    alias command.
        out.append(self.startup.generate())
        
        # 6. Write out main.cfg, and generate folders.
        os.makedirs(self.name_space, exist_ok=True)
        os.makedirs(self.name_space+"/file", exist_ok=True)
        maincfg = open(self.name_space+"/main.cfg", "wb")
        maincfg.write(("\n".join(out)+"\n").encode("utf-8"))
        maincfg.close()
        
        # 7. Create all Indirect files - the files that contain echo statements
        #    or anything with special characters.
        for i, fs in enumerate(self.file_stash):
            # Generate index directories
            os.makedirs(self.name_space + "/file/%0.1X" % i, exist_ok=True)
            for fc in fs:
                # Write out each file in the index directory
                fcfg = open(self.name_space + "/file/%0.1X/%s.cfg"
                            % (i, fc.real_name()), "wb")
                fcfg.write(fc.generate().encode("utf-8"))
                fcfg.close()

    def register(self):
        """
        Wrapper around Command.register() that avoids adding to the root
        registry.
        """
        self.eval_state = COMMAND_EVAL_REGISTER
        for ch in self.children:
            if ch.eval_state == COMMAND_EVAL_NONE:
                ch.register()

    def get_error_name(self):
        """
        See misc/logging.py.
        """
        return self.name_prefix
