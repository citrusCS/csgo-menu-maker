COMMAND_EVAL_NONE = 0
COMMAND_EVAL_REGISTER = 1
COMMAND_EVAL_COMBINE = 2


class Command:
    """
    Represents an 'alias' Source engine console command.

    A Command instance can have multiple children, and thus resembles a tree
    structure. By allowing nesting in commands, complex constructs can be
    created in an organized manner. The Command class is inherited by almost
    every other class in this package.
    """
    def __init__(self, parent, cls):
        # Set neighbors
        self.parent = parent
        self.root = self.parent.root
        self.children = []

        # Set identifying information
        self.cls = cls
        self.id = self.root.get_next_id()
        self.name = ""

        # Miscellaneous edge-case flags
        self.obf_name = None
        self.is_obf = False
        self.eval_state = COMMAND_EVAL_NONE
        self.clean = False
        self.hide_children = False
        self.state_prefix = ""
        self.state_prefix_other = None

        # Recognize parent by adding this as a child
        self.parent.children.append(self)

    def __str__(self):
        """
        Return a string representation of the Command's identifying properties.

        If the command's name has been mangled (obfuscated), the obfuscated
        version is returned instead.
        """
        if not self.is_obf:
            if self.name == "":
                # Anonymous mode: just return parent, id, class.
                return str(self.parent) + "." + self.cls + "-" + str(self.id)
            else:
                # Has name: return all of the above + name.
                return str(self.parent) + "." + self.cls + "-" + str(self.id) \
                        + "_" + self.name
        else:
            # If we're obfuscated, just return the mangled name.
            return self.obf_name

    def __add__(self, other):
        """
        Concatenate the names of two commands.

        Only used in Command.__str__() for determining the name of the parent.
        """
        if type(other) == str:
            return str(self) + other

    def __iadd__(self, other):
        """
        Used to append a child, but without linking it to this object.

        Consider it analogous to a link in the filesystem, where the pointed-to
        object has a different parent than the source pointer.
        """
        self.children.append(other)
        return self

    def register(self):
        """
        Pre-process this command and its children in order to calculate a list
        of all commands in the tree.

        Only called by Root. Acts 'smart', i.e. will only add it to the
        registry if it hasn't been added yet.
        """
        # Set the evaluation state of this instance to REGISTER, as it has been
        # recognized by the root object.
        self.root.registry.append(self)
        self.eval_state = COMMAND_EVAL_REGISTER

        # Loop through children and register them too, recursively.
        for ch in self.children:
            # Only register the child if it has not been registered yet;
            # therefore its evaluation state has been set to NONE.
            if ch.eval_state == COMMAND_EVAL_NONE:
                ch.register()

    def combine(self):
        """
        Return an executable string of console commands representing this
        instance and possibly its children.

        Will only evaluate children if combine() hasn't been called on them
        yet.
        """
        # If the contents of this command should be hidden from the main .cfg,
        # discard them.
        if self.hide_children:
            return ""

        # Set the evaluation state of this instance to COMBINE, as its code has
        # been generated.
        self.eval_state = COMMAND_EVAL_COMBINE

        # output will store the contents of this instance; meaning its code and
        # the code of its children.
        output = []

        # Loop through children and evaluate them.
        for ch in self.children:
            # Only evaluate children if they haven't been yet (i.e., their eval
            # state is not COMMAND_EVAL_COMBINE)
            if ch.eval_state == COMMAND_EVAL_REGISTER:
                gen = ch.generate()
                if gen is not None:
                    output.append('alias "'+str(ch)+'" "'+gen+'"')
                output.extend(ch.combine())

        return output

    def generate(self):
        """
        Return an executable string of console commands representing this
        instance only. Overrideable.
        """
        return ""

    def get_error_name(self):
        """
        Return a string formatted so that it can be printed in an error msg.
        """
        if hasattr(self, "ui_name"):
            # If this instance is part of the UI (has attribute "ui_name"), use
            # that to form a "pretty" error message.
            return self.parent.get_error_name()+"."+self.ui_name
        else:
            # If not, revert to the regular way.
            if self.name == "":
                return self.parent.get_error_name() + "." + self.cls + "-" \
                        + str(self.id)
            else:
                return self.parent.get_error_name() + "." + self.cls + "_" \
                        + self.name

    def real_name(self):
        if self.is_obf:
            return self.obf_name
        else:
            return self.name
