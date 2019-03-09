import copy

component_name_space = []
type_mapping = {}


def name_space(*args, **kwargs):
    """
    Append/pop to the global namespace path.
    """
    if len(args):
        component_name_space.append((args[0], kwargs))
    else:
        component_name_space.pop()


class Component:
    """
    Decorator to add a class to the global type mapping.
    """
    def __init__(self, type_name, *args, **kwargs):
        self.aliases = []
        self.name_space = copy.copy(component_name_space)
        self.type_name = self.make_type_name(type_name)
        self.kwargs = kwargs
        self.args = args
        if len(self.args):
            self.aliases = self.args

    def __call__(self, cls):
        type_mapping[self.type_name] = cls
        for a in self.aliases:
            type_mapping[self.make_type_name(a)] = self.type_name
        cls.type_name = self.type_name
        cls.name_space = self.name_space
        cls.aliases = self.aliases
        return cls

    def make_type_name(self, n):
        return ".".join(
            [j[0] for j in self.name_space] + [n, ]
        )
