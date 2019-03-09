import copy

from .. import command
from .. import menu
from ..param import *

from .component import *

name_space("generic")


@Component("choice")
class Choice(menu.Choice):
    params = ParamObj(
        Name("Generic Chooser"),
        Desc("Choose between different sets of commands."),
        Flex(
            "choices",
            String(
                "name",
                description="The choice's name."
            ),
            Sequence(
                "commands",
                description="The commands that make up this choice.",
                seqtypes=str,
                zerook=True,
                default=[],
                ex_vals=[
                    [
                        "echo Hello World"
                    ]
                ]
            ),
            flexkey=None,
            description=(
                "The different choices that make up this component's contents."
            )
        )
    )

    def __init__(self, parent, options):
        menu.Choice.__init__(self, parent, options)
        for ch in self.params["choices"]:
            comp = command.Compound(self)
            for c in ch["commands"]:
                command.Primitive(comp, c, [])
            self.add_choice(ch["name"], comp)
        self.make_choices()


@Component("choicevar", "choice_var")
class ChoiceVar(menu.ChoiceVar):
    params = ParamObj(
        Name("Generic Var Chooser"),
        Desc("Choose between different states for a convar."),
        String(
            "convar",
            description="The variable to be changed."
        ),
        Sequence(
            "choices",
            description="The different states for the convar.",
            seqtypes=str
        )
    )

    def __init__(self, parent, options):
        menu.ChoiceVar.__init__(self, parent, options)
        self.var = self.params["convar"]
        for ch in self.params["choices"]:
            self.choices.append(str(ch))
        self.make_choices()


@Component("choicevarbinary", "choice_var_binary")
class ChoiceVarBinary(menu.ChoiceVarBinary):
    params = ParamObj(
        Name("Generic Binary Var Chooser"),
        Desc("Choose between different two different states for a convar."),
        String(
            "convar",
            description="The variable to be changed."
        ),
        Binary(
            "default",
            default=False,
            description="The default value."
        )
    )

    def __init__(self, parent, options):
        menu.ChoiceVarBinary.__init__(self, parent, options)
        self.var = self.params["convar"]
        self.default = self.params["default"]
        self.make_choices()


@Component("fireable")
class Fireable(menu.Fireable):
    params = ParamObj(
        Name("Generic Fireable"),
        Desc("Run a one-off set of commands."),
        String(
            "text",
            description="The text that will be shown in the UI."
        ),
        Sequence(
            "commands",
            description="The different commands that should be run.",
            seqtypes=str
        )
    )

    def __init__(self, parent, options):
        menu.Fireable.__init__(self, parent, options)
        self.set_command(self.params["commands"])
        self.text = self.params["text"]
        self.make_choices()


@Component("fireablecmd", "fireable_cmd")
class FireableCmd(menu.FireableCmd):
    params = ParamObj(
        Name("Generic Fireable"),
        Desc("Run a single command."),
        String(
            "text",
            description="The text that will be shown in the UI.",
            default=None
        ),
        String(
            "concmd",
            description="The command that will be run."
        )
    )

    def __init__(self, parent, options):
        menu.FireableCmd.__init__(self, parent, options)
        self.set_command(self.params["concmd"])
        if self.params["text"] is None:
            self.text = self.params["concmd"]
        else:
            self.text = self.params["text"]
        self.make_choices()


@Component("bar")
class Bar(menu.Bar):
    params = ParamObj(
        Name("Generic Bar"),
        Desc("Set a value visually."),
        Number(
            "min",
            description="The minimum value for the bar (left value)."
        ),
        Number(
            "max",
            description="The maximum value for the bar (right value)."
        ),
        Number(
            "steps",
            description="The number of steps between the min and max values.",
            int=True,
            ex_vals=[20]
        ),
        String(
            "convar",
            description="The convar that will be changed."
        ),
        String(
            "style",
            choices=["int", "percent", "str"],
            description="How the number will be displayed."
        ),
        String(
            "strleft",
            default="",
            description=(
                "For style 'str', what string to be displayed on the left side"
                " of the bar."
            )
        ),
        String(
            "strright",
            default="",
            description=(
                "For style 'str', what string to be displayed on the right"
                " side of the bar."
            )
        ),
        Number(
            "default",
            description="The default number shown.",
            default=0
        )
    )

    def __init__(self, parent, options):
        menu.Bar.__init__(self, parent, options)
        self.min = self.params["min"]
        self.max = self.params["max"]
        self.steps = self.params["steps"]
        self.var = self.params["convar"]
        self.style = self.params["style"]
        self.strleft = self.params["strleft"]
        self.strright = self.params["strright"]
        self.default = self.params["default"]
        self.make_choices()


@Component("message")
class Message(menu.Message):
    params = ParamObj(
        Name("Generic Message"),
        Desc("A message box."),
        String(
            "text",
            description="The text that will be shown in the UI."
        )
    )

    def __init__(self, parent, options):
        menu.Message.__init__(self, parent, options)
        self.text = self.params["text"]
        self.make_choices()


class PresetChooser(menu.PresetChooser):
    params = ParamObj(
        Name("Generic Preset Chooser"),
        Desc("Choose presets."),
        Flex(
            "presets",
            String(
                "inherit",
                description="The preset that will be inherited from.",
                default=None
            ),
            String(
                "name",
                description="The name of the preset."
            ),
            flexkey="inherit",
            description="The presets that will be used."
        )
    )

    def __init__(self, parent, options, partype):
        self.partype = partype
        self.partype.register(self)
        menu.PresetChooser.__init__(self, parent, options)
        for i, pset in enumerate(self.params["presets"]):
            cmds = []
            if hasattr(self, "get_commands_seq"):
                cmds.extend(self.get_commands_seq(pset, i))
            else:
                cmds.extend(self.get_commands(pset))
            self.add_preset(pset["name"], cmds)
            self.menu_root.add_preset_cmds(
                self.preset_type,
                pset["name"],
                cmds
            )
        self.make_choices()

    def flex_callback(self, obj, after):
        """
        Before evaluating preset params, this is called in order to merge
        the inherited properties if they aren't in the class yet.
        """
        if "inherit" in after and after["inherit"] is not None:
            pseti = self.menu_root.get_preset(
                self.preset_type,
                after["inherit"]
            )
            for k in pseti:
                if k not in obj:
                    after[k] = pseti[k]
        if "name" in after and after["name"] is not None:
            self.menu_root.add_preset(self.preset_type, after["name"], after)
        return after

    def get_params(self, cur_type):
        """
        Overridden because the child class will always pass a custom parameter
        that needs to be merged as it isn't in the type object.
        """
        newpars = copy.deepcopy(cur_type.params)
        newpars.register(self)
        if cur_type == PresetChooser:
            newpars.children["presets"].merge(self.partype)
            newpars.children["presets"].callback = self.flex_callback
        return (newpars, cur_type.__base__)

    def make_param_cmd(self, obj, key):
        """
        Convenience method to bind convars from param objects to real concmds.
        """
        comp = self.params.children["presets"].children
        param = comp[key]
        if not isinstance(param, Sequence):
            return command.Primitive(
                self,
                param.kwargs["convar"],
                str(obj[key])
            )
        else:
            out = []
            for i, v in enumerate(obj[key]):
                out.append(
                    command.Primitive(
                        self,
                        param.kwargs["convar"][i],
                        str(obj[key][i])
                    )
                )
            return out


name_space()
