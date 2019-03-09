import inspect
import pathlib
import urllib.parse

import yaml
import yattag

from .. import component
from .. import loader
from .. import misc
from .. import param

FLAG_DATA = {
    "cheat": {
        "label": "command",
        "message": "cheat",
        "alt":
            "This component is a cheat or triggers a cheat and cannot be used"
            " on most servers.",
        "color": "b71c1c"
    },
    "replicated": {
        "label": "command",
        "message": "replicated",
        "alt":
            "This component modifies a console variable that is replicated,"
            " meaning it can only be modified by server operators and it is"
            " changed (replicated) on all connected clients.",
        "color": "b71c1c"
    },
    "needs_fireable": {
        "label": "bug",
        "message": "needs fireable",
        "alt":
            "The action triggered by this component modifies some internal"
            " write-only state. Thus, the behavior of this component may be"
            " inpredictable if used as a choice menu.",
        "color": "1e8835"
    }
}


class DocGen(misc.Loggable):
    """
    Documentation generator.

    Takes all component class listings, and translates them into a big
    component reference to be used on the wiki.
    """

    def __init__(self):
        self.component_mapping = {}
        self.component_pages = {}
        self.shields = {}
        self.get_components()
        self.make_all()

    def get_components(self):
        """
        Update self.component_mapping with pairs of key type_name and value
        object class.
        """
        for type_name, cls in component.type_mapping.items():
            if isinstance(cls, str):
                continue
            self.component_mapping[type_name] = cls

    def make_shield(self, doc, tag, text, **kwargs):
        """
        Return an inline-formatted shields.io shield image link, with kwargs
        subbed in as url arguments.
        """
        alt = ""
        if "alt" in kwargs:
            alt = kwargs["alt"]
            kwargs.pop("alt")
        link = "https://img.shields.io/static/v1.svg?"
        link += urllib.parse.urlencode(kwargs)
        with tag("img", src=link, alt=alt, title=alt):
            text(" ")

    def make_class_name(self, cls):
        mod = inspect.getmodule(cls).__name__
        mod = ".".join(mod.split(".")[1:])
        return mod + "." + cls.__name__

    def make_link_to_class(self, cls):
        """
        Generate a link that points to the implementation of class cls.
        """
        def_file = inspect.getsourcefile(cls)
        def_line = inspect.getsourcelines(cls)[1]

        # Need to manipulate the path because it is an absolute path which
        # isn't suitable for a github URL.
        path = pathlib.Path(def_file)
        parts = path.parts
        out_path = list(parts)
        p = out_path[0]
        while p is not "csgomenumaker":
            out_path.pop(0)
            p = out_path[0]

        return \
            "https://www.github.com/citrusCS/csgo-menu-maker/tree/master" \
            "/%s#L%i" % ("/".join(out_path), def_line)

    def make_comp_flags(self, comp, doc, tag, text):
        """
        Generate flag image links for each flag in `comp.kwargs`.
        """
        # if "version" not in comp.params.kwargs:
        #     self.error("Missing version for component %s!" % comp)
        # self.make_shield(
        #     doc,
        #     tag,
        #     text,
        #     label="version",
        #     message=comp.params.kwargs["version"],
        #     alt=
        #         "The version of csgomenumaker that this component was"
        #         " introduced in.",
        #     color="8c42f4"
        # )
        if "flags" in comp.params.kwargs:
            if len(comp.params.kwargs):
                for flag in comp.params.kwargs["flags"]:
                    # sio_params = the params to give to shields.io
                    sio_params = {}
                    if flag in FLAG_DATA:
                        sio_params = FLAG_DATA[flag]
                    else:
                        self.error(
                            "Unrecognized flag '%s' in component '%s'" %
                            (
                                flag,
                                comp
                            )
                        )
                    self.make_shield(doc, tag, text, **sio_params)

    def make_comp_description(self, comp, doc, tag, text):
        """
        Render the description of `comp` to `doc`.
        """
        if "desc" not in comp.params.children:
            self.error("No desc for component '%s'" % comp)

        with tag("p"):
            text(comp.params.children["desc"].kwargs["default"])

    def make_comp_details(self, comp, doc, tag, text):
        """
        Add a component's details section to doc.
        """

        # Ensure that the required data is included
        params = comp.params
        if "name" not in params.children:
            self.error("No name for component '%s'" % comp)
        if "desc" not in params.children:
            self.error("No desc for component '%s'" % comp)

        with tag("table"):
            # 1. Default Name
            with tag("tr"):
                with tag("td"):
                    text("Default Name")
                with tag("td"):
                    text(comp.params.children["name"].kwargs["default"])
            # 2. Default Description
            with tag("tr"):
                with tag("td"):
                    text("Default Description")
                with tag("td"):
                    text(comp.params.children["desc"].kwargs["default"])
            # 3. Flags
            with tag("tr"):
                with tag("td"):
                    text("Flags")
                with tag("td"):
                    if "flags" in comp.params.kwargs:
                        if len(comp.params.kwargs["flags"]):
                            first = True
                            for flag in comp.params.kwargs["flags"]:
                                if first:
                                    first = False
                                else:
                                    text(" ")
                                with tag("code"):
                                    text(flag)
                        else:
                            text("None")
                    else:
                        text("None")
            # 4. Definition
            with tag("tr"):
                with tag("td"):
                    text("Definition")
                with tag("td"):
                    # Definition requires two components - the code name and
                    # a link to the implementation
                    with tag("code"):
                        text(self.make_class_name(comp))
                    text(" - ")
                    with tag("a", href=self.make_link_to_class(comp)):
                        text("source")
            # 5. Parent
            with tag("tr"):
                with tag("td"):
                    text("Base")
                with tag("td"):
                    base = comp.__base__
                    # Similarly requires two components
                    with tag("code"):
                        text(self.make_class_name(base))
                    text(" - ")
                    with tag("a", href=self.make_link_to_class(base)):
                        text("source")

    def make_kwarg_value(self, kwval):
        """
        Format a value for a parameter keyword argument.
        """
        if isinstance(kwval, str):
            return '"%s"' % kwval
        elif isinstance(kwval, (list, tuple)):
            out = []
            for i in kwval:
                if isinstance(i, type):
                    if i.__name__ == "int" or i.__name__ == "float":
                        out.append("Number")
                    elif i.__name__ == "str":
                        out.append("String")
                else:
                    out.append(str(i))
            return ", ".join(out)
        return str(kwval)

    def make_comp_params(self, comp, param, doc, tag, text):
        """
        Recursively add a param's listing to doc.
        """
        if "nodoc" in param.kwargs and param.kwargs["nodoc"]:
            return

        with tag("h4"):
            with tag("code"):
                text(param.key)
        with tag("dl"):
            with tag("dd"):
                typn = type(param).__name__.lower()
                self.make_shield(
                    doc,
                    tag,
                    text,
                    label="type",
                    message=typn,
                    color="004c80"
                )
                for kwarg, val in sorted(
                    param.kwargs.items(),
                    key=lambda l: l[0]
                ):
                    if kwarg in ["model", "nodoc", "ex_vals"]:
                        continue
                    fval = self.make_kwarg_value(val)
                    if kwarg == "default":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="default",
                            message=fval,
                            color="198000",
                            alt=(
                                "The default value for this parameter"
                                " is %s." % fval
                            )
                        )
                    elif kwarg == "description":
                        pass
                    elif kwarg == "int":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="precision",
                            message="int",
                            color="805700",
                            alt=(
                                "Values for this parameter should be clamped"
                                " to integer values."
                            )
                        )
                    elif kwarg == "max":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="max",
                            message=fval,
                            color="805700",
                            alt=(
                                "Values for this parameter should be kept"
                                " under %s." % fval
                            )
                        )
                    elif kwarg == "min":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="min",
                            message=fval,
                            color="805700",
                            alt=(
                                "Values for this parameter should be kept"
                                " above %s." % fval
                            )
                        )
                    elif kwarg == "choices":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="choices",
                            message=fval,
                            color="805700",
                            alt=(
                                "Values for this parameter should be one of"
                                " %s." % fval
                            )
                        )
                    elif kwarg == "flexkey":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="identifier value",
                            message=fval,
                            color="805700",
                            alt=(
                                "Anonymous sub-values will be interpreted as"
                                " the key %s." % fval
                            )
                        )
                    elif kwarg == "flexkeyname":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="identifier key",
                            message=fval,
                            color="805700",
                            alt=(
                                "Anonymous sub-keys will be interpreted as"
                                " the key %s." % fval
                            )
                        )
                    elif kwarg == "seqtypes":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="sequence types",
                            message=fval,
                            color="805700",
                            alt=(
                                "Value types for this sequence parameter"
                                " should be one of %s." % fval
                            )
                        )
                    elif kwarg == "zerook":
                        self.make_shield(
                            doc,
                            tag,
                            text,
                            label="sequence types",
                            message=fval,
                            color="805700",
                            alt=(
                                "Values for this sequence parameter may be "
                                " zero in length."
                            )
                        )
                    else:
                        self.error(
                            "Unrecognized kwarg '%s' in component '%s'" %
                            (
                                kwarg,
                                comp
                            )
                        )
                with tag("p"):
                    text(param.kwargs["description"])
        with tag("dl"):
            with tag("dd"):
                for _, par in sorted(param.children.items()):
                    self.make_comp_params(comp, par, doc, tag, text)

    def make_comp_example(self, comp):
        return "tree:\n    %s: %s\n" % (
            comp.params.children["name"].kwargs["default"],
            comp.type_name
        )

    def make_comp(self, comp, doc, tag, text):
        """
        Add a component's listing to doc.
        """

        # Make the header
        with tag("h3"):
            with tag("code"):
                text(comp.type_name)

        # Make the flags
        self.make_comp_flags(comp, doc, tag, text)

        # Make the aliases
        if len(comp.aliases):
            with tag("p"):
                text("Aliases: ")
                first = True
                for al in comp.aliases:
                    if first:
                        first = False
                    else:
                        text(", ")
                    with tag("code"):
                        text(al)

        # Make the description
        self.make_comp_description(comp, doc, tag, text)

        # Make the info section
        with tag("details"):
            with tag("summary"):
                with tag("b"):
                    text("Info")
            with tag("dl"):
                with tag("dd"):
                    self.make_comp_details(comp, doc, tag, text)

        # Make the params section
        with tag("details"):
            with tag("summary"):
                with tag("b"):
                    text("Parameters")
            with tag("dl"):
                with tag("dd"):
                    for _, param in sorted(comp.params.children.items()):
                        self.make_comp_params(comp, param, doc, tag, text)

        # Make a horizontal line to finish it off
        with tag("hr", width="60%"):
            pass

    def make_all(self):
        """
        Initialize a yattag.Doc instance and start going.
        """

        doc, tag, text = yattag.Doc().tagtext()
        for comp_name in sorted(self.component_mapping.keys()):
            comp = self.component_mapping[comp_name]
            self.make_comp(comp, doc, tag, text)
        print(doc.getvalue())
