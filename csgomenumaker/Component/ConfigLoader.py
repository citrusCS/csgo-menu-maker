import yaml

from .. import Command
from .. import Component
from .. import Menu


class ConfigLoader(Menu.Menu):
    def __init__(self, infile):
        self.options = yaml.load(open(infile, "r"))
        self.root = Command.Root()
        self.root.setConfig(self)
        self.settings = self.optValue(self.options, "settings", dict())
        self.addClasses()
        self.addSounds()
        self.addGlobals()
        self.addGlobalsNav()
        self.makeAll()

    def addClasses(self):
        for cls in Component.ConfigTypeMapping.keys():
            self.root.addClass(cls, Component.ConfigTypeMapping[cls])

    def addGlobals(self):
        self.root.addGlobal("void", Command.Null(self.root))
        filterIndir = Command.Indirect(self.root)
        Command.Primitive(
            filterIndir,
            "con_filter_enable",
            [1]
        )
        Command.Primitive(
            filterIndir,
            "con_filter_text",
            ['"'+self.root.filterChar+'"']
        )
        Command.Primitive(
            filterIndir,
            "con_filter_text_out",
            ['"'+self.root.filterCharOut+'"']
        )
        self.root.addGlobal(
            "filter.set",
            filterIndir
        )
        self.root.addGlobal(
            "filter.reset",
            Command.Primitive(
                self.root,
                "con_filter_enable",
                [0]
            )
        )
        self.root.addGlobal(
            "clear",
            Command.Primitive(
                self.root,
                "clear",
                []
            )
        )
        self.root.addGlobal(
            "developer.set",
            Command.Primitive(
                self.root,
                "developer",
                [1]
            )
        )
        self.root.addGlobal(
            "developer.reset",
            Command.Primitive(
                self.root,
                "developer",
                [0]
            )
        )

    def addGlobalsNav(self):
        toMake = [
            "nav.up",
            "nav.down",
            "nav.left",
            "nav.right",
            "nav.fire",
            "nav.back",
            "nav.enable"
        ]
        sounds = [
            "updown",
            "updown",
            "leftright",
            "leftright",
            "forward",
            "backward",
            None
        ]
        keySettings = self.optValue(self.settings, "keybinds", dict())
        self.keybinds = {
            "up":       self.optValue(keySettings, "up", "uparrow"),
            "down":     self.optValue(keySettings, "down", "downarrow"),
            "left":     self.optValue(keySettings, "left", "leftarrow"),
            "right":    self.optValue(keySettings, "right", "rightarrow"),
            "fire":     self.optValue(keySettings, "use", "enter"),
            "back":     self.optValue(keySettings, "back", "\\"),
            "enable":   self.optValue(keySettings, "enable", "alt")
        }
        for i, n in enumerate(toMake):
            if sounds[i] is not None:
                self.root.addGlobal(
                    n+"_real",
                    Command.Compound(self.root)
                )
                self.root.getGlobal(n+"_real").addChild(
                    self.root.getGlobal("sound_"+sounds[i])
                )
                self.root.addGlobal(
                    n,
                    Command.Null(
                        self.root.getGlobal(n+"_real")
                    )
                )
            else:
                plusSt = Command.Compound(self.root)
                plusSt.statePrefix = "+"
                self.root.addGlobal(n+"_real", plusSt)
                minusSt = Command.Compound(self.root)
                minusSt.statePrefix = "-"
                plusSt.statePrefixOther = minusSt
                for i, m in enumerate(toMake):
                    if m == n:
                        continue
                    part = m.split(".")[1]
                    Command.Primitive(
                        plusSt,
                        "bind",
                        [
                            self.keybinds[part],
                            self.root.getGlobal(m+"_real")
                        ]
                    )
                    Command.Primitive(minusSt, "unbind", [self.keybinds[part]])
                indir = Command.Indirect(plusSt)
                indir.addChild(self.root.getGlobal("developer.set"))
                self.root.addGlobal(
                    n,
                    Command.Placeholder(
                        indir,
                        self.root.getGlobal("void")
                    )
                )
                minusSt.addChild(
                    self.root.getGlobal("developer.reset")
                )
                self.root.addBind(
                    self.keybinds["enable"],
                    self.root.getGlobal(n+"_real")
                )

    def addSounds(self):
        sndSettings = self.optValue(self.settings, "sounds", dict())
        sndVolume = self.optValue(sndSettings, "volume", 0.8)
        self.root.addGlobal(
            "sound_updown",
            Command.Primitive(
                self.root,
                "playvol",
                [
                    self.optValue(sndSettings, "updown", "buttons/button22"),
                    str(sndVolume)
                ]
            )
        )
        self.root.addGlobal(
            "sound_leftright",
            Command.Primitive(
                self.root,
                "playvol",
                [
                    self.optValue(sndSettings, "leftright", "ui/menu_accept"),
                    str(sndVolume)
                ]
            )
        )
        self.root.addGlobal(
            "sound_forward",
            Command.Primitive(
                self.root,
                "playvol",
                [
                    self.optValue(sndSettings, "forward", "ui/menu_focus"),
                    str(sndVolume)
                ]
            )
        )
        self.root.addGlobal(
            "sound_backward",
            Command.Primitive(
                self.root,
                "playvol",
                [
                    self.optValue(sndSettings, "backward", "ui/menu_back"),
                    str(sndVolume)
                ]
            )
        )
        self.root.addGlobal(
            "sound_fire",
            Command.Primitive(
                self.root,
                "playvol",
                [
                    self.optValue(sndSettings, "fire", "buttons/button14"),
                    str(sndVolume)
                ]
            )
        )

    def makeAll(self):
        j = Menu.Root(self.root, self.options)
        j.joinChildren()
        j.makeReAliases()
        self.root.getGlobal("nav.enable")
        self.root.setStartup(j.selections[0].getAction("entry"))
        self.root.makeAll()
        print(
            (
                "Generation finished! Move the new '%s' folder to your " +
                "csgo cfg directory, and add this line to your autoexec:"
            ) %
            self.root.nameSpace
        )
        print("exec " + self.root.nameSpace + "/main.cfg")
        print("You may also test it by running the command in the console.")

    def error(self, s):
        print("\x1b[31mError: %s" % s)
        sys.exit(1)
