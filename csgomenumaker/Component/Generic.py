from .. import Menu

from .ConfigType import ConfigType


@ConfigType("generic.choice")
class Choice(Menu.Choice):
    defaultName = "Generic Chooser"
    defaultDesc = "Choose between different sets of commands."

    def __init__(self, parent, options):
        Menu.Choice.__init__(self, parent, options)
        self.optTypeKey(options, "choices", list())
        for ch in options["choices"]:
            self.optType(ch, dict())
            self.optTypeKey(ch, "commands", list())
            self.optTypeKey(ch, "name", str())
            self.addChoice(ch["name"], self.makeCmdList(ch["commands"]))
        self.makeChoices()


@ConfigType("generic.fireable")
class Fireable(Menu.Fireable):
    defaultName = "Generic Fireable"
    defaultDesc = "Run a one-off command."

    def __init__(self, parent, options):
        Menu.Fireable.__init__(self, parent, options)
        self.optTypeKey(options, "commands", list())
        self.optTypeKey(options, "text", str())
        self.setCommand(self.makeCmdList(options["commands"]))
        self.setText(options["text"])
        self.makeChoices()


@ConfigType("generic.bar")
class Bar(Menu.Bar):
    defaultName = "Generic Bar"
    defaultDesc = "Set a value visually."

    def __init__(self, parent, options):
        Menu.Bar.__init__(self, parent, options)
        self.optTypeKey(options, "min", float())
        self.optTypeKey(options, "max", float())
        self.optTypeKey(options, "steps", float())
        self.optTypeKey(options, "var", str())
        self.setMin(options["min"])
        self.setMax(options["max"])
        self.setSteps(options["steps"])
        self.setVar(options["var"])
        self.setStyle(self.optValue(options, "style", "int"))
        self.setDefault(self.optValue(options, "default", options["min"]))
        self.makeChoices()


@ConfigType("generic.message")
class Message(Menu.Message):
    defaultName = "Generic Message"
    defaultDesc = "A message box."

    def __init__(self, parent, options):
        Menu.Message.__init__(self, parent, options)
        self.optTypeKey(options, "text", str())
        self.setText(options["text"])
        self.makeChoices()
