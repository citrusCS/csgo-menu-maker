from .. import Command

from .Menu import Menu
from .Choice import Choice


class PresetChooser(Choice):
    def __init__(self, parent, options):
        Choice.__init__(self, parent, options)
        self.presetType = ""
        if "presets" not in self.options:
            self.error("Expected 'presets' parameter in object '%s'" % options)
        if isinstance(options["presets"], dict):
            self.optLenZero(options["presets"])
            for name in options["presets"].keys():
                self.optTypeKey(options["presets"], name, dict())
                if "name" not in options["presets"][name].keys():
                    options["presets"][name]["name"] = name
                self.makeChild(options["presets"][name])
        elif isinstance(options["presets"], list):
            self.optLenZero(options["presets"])
            for child in options["presets"]:
                self.makeChild(child)
        else:
            self.error("Expected list or object type for 'presets' parameter")
        self.makeChoices()

    def makeChild(self, pre):
        self.optType(pre, dict())
        cmds = self.getCommands(pre)
        self.optTypeKey(pre, "name", str())
        self.addPreset(pre["name"], cmds)

    def setPresetType(self, ptype):
        self.presetType = ptype

    def addPreset(self, name, commands):
        ocmd = Command.Compound(self)
        for cmd in commands:
            ocmd.addChild(cmd)
        self.addChoice(name, ocmd)
        self.menuRoot.addPreset(self.presetType, name, ocmd)
