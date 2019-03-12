import yaml

from .. import command
from .. import component
from .. import menu
from .. import misc

from .settings import Settings


class Loader(misc.Loggable):
    """
    The class that actually loads the damn config.

    Holds the YAML instance with the config file, and holds the command.Root of
    the entire operation.
    """

    def __init__(self, infile, file=True, example=False):
        if file:
            self.options = yaml.safe_load(open(infile, "r"))
        else:
            self.options = yaml.safe_load(infile)
        self.example = example
        self.root = command.Root()
        self.root.config = self
        self.root.example = self.example
        self.root.virtual = self.example
        self.settings = Settings(self.options).get_settings()
        for cls in component.type_mapping.keys():
            self.root.class_mapping[cls] = component.type_mapping[cls]
        self.add_sounds()
        self.add_globals()
        self.add_globals_nav()
        self.make_all()

    def add_globals(self):
        """
        Add all globals that are used by the command system.
        """
        # void is a "null pointer" that does nothing but does it gracefully
        self.root.globals["void"] = command.Null(self.root)
        # Filter commands - these don't work because of a stupid bug. Unused.
        filter_indir = command.Indirect(self.root)
        command.Primitive(
            filter_indir,
            "con_filter_enable",
            [1]
        )
        command.Primitive(
            filter_indir,
            "con_filter_text",
            ['"'+self.root.filter_char+'"']
        )
        command.Primitive(
            filter_indir,
            "con_filter_text_out",
            ['"'+self.root.filter_char_out+'"']
        )
        self.root.globals["filter.set"] = filter_indir
        self.root.globals["filter.reset"] = \
            command.Primitive(
                self.root,
                "con_filter_enable",
                [0]
            )
        self.root.globals["clear"] = \
            command.Primitive(
                self.root,
                "clear",
                []
            )
        # Developer toggles - used when pressing enable.
        self.root.globals["developer.set"] = \
            command.Primitive(
                self.root,
                "developer",
                [1]
            )
        self.root.globals["developer.reset"] = \
            command.Primitive(
                self.root,
                "developer",
                [0]
            )

    def add_globals_nav(self):
        """
        Add keybind globals, bind keys, and attach sounds to each key.
        """
        # These are the nav global names.
        to_make = [
            "nav.up",
            "nav.down",
            "nav.left",
            "nav.right",
            "nav.fire",
            "nav.back",
            "nav.enable"
        ]
        # These are the keys for each sound, mapped to each nav global name.
        sounds = [
            "updown",
            "updown",
            "leftright",
            "leftright",
            "forward",
            "backward",
            None
        ]
        self.keybinds = self.settings["keybinds"]
        for i, n in enumerate(to_make):
            if sounds[i] is not None:
                # This isn't enable, which is special
                self.root.globals[n+"_real"] = command.Compound(self.root)
                self.root.globals[n+"_real"].children.append(
                    self.root.globals["sound."+sounds[i]]
                )
                # Bind the global to null. It will be rebound when the user
                # presses enable.
                self.root.globals[n] = \
                    command.Null(
                        self.root.globals[n+"_real"]
                    )
            else:
                # This is enable. Special case. Bind two states for the
                # command, + and -. They each turn on/off developer mode.
                plus_st = command.Compound(self.root)
                plus_st.state_prefix = "+"
                self.root.globals[n+"_real"] = plus_st
                minus_st = command.Compound(self.root)
                minus_st.state_prefix = "-"
                plus_st.state_prefix_other = minus_st

                # Then, make pressing enable bind/unbind the other six
                # keybind'd keys.
                for i, m in enumerate(to_make):
                    if m == n:
                        continue
                    part = m.split(".")[1]
                    command.Primitive(
                        plus_st,
                        "bind",
                        [
                            self.keybinds[part],
                            self.root.globals[m+"_real"]
                        ]
                    )
                    command.Primitive(
                        minus_st,
                        "unbind",
                        [self.keybinds[part], ]
                    )

                # Place developer setup in an indirect in case source goes
                # sicko mode on me.
                indir = command.Indirect(plus_st)
                indir.children.append(self.root.globals["developer.set"])
                self.root.globals[n] = \
                    command.Placeholder(
                        indir,
                        self.root.globals["void"]
                    )
                minus_st.children.append(
                    self.root.globals["developer.reset"]
                )
                self.root.binds[self.keybinds["enable"]] = \
                    self.root.globals[n+"_real"]

    def add_sounds(self):
        """
        Add sound globals based off of their setting values.
        """
        snd_volume = self.settings["sounds"]["volume"]

        self.root.globals["sound.updown"] = \
            command.Primitive(
                self.root,
                "playvol",
                [
                    self.settings["sounds"]["updown"],
                    str(snd_volume)
                ]
            )

        self.root.globals["sound.leftright"] = \
            command.Primitive(
                self.root,
                "playvol",
                [
                    self.settings["sounds"]["leftright"],
                    str(snd_volume)
                ]
            )

        self.root.globals["sound.forward"] = \
            command.Primitive(
                self.root,
                "playvol",
                [
                    self.settings["sounds"]["forward"],
                    str(snd_volume)
                ]
            )

        self.root.globals["sound.backward"] = \
            command.Primitive(
                self.root,
                "playvol",
                [
                    self.settings["sounds"]["backward"],
                    str(snd_volume)
                ]
            )

    def make_all(self):
        # The __main__ of this whole module. This is where the magic happens.
        # Create a root menu with options. It calls recursively, we're good.
        j = menu.Root(self.root, self.options)
        self.menu_root = j
        j.join_children()
        j.make_realiases()
        # Set the startup command to the entry of the first menu.
        self.root.startup = j.selections[0].actions["entry"]
        # Make everything.
        self.root.make_all()
        if self.example:
            return
        print(
            (
                "Generation finished! Move the new '%s' folder to your " +
                "csgo cfg directory, and add this line to your autoexec:"
            ) %
            self.root.name_space
        )
        print("exec " + self.root.name_space + "/main.cfg")
        print("You may also test it by running the command in the console.")

    def getErrorName(self):
        return "<top-level config>"
