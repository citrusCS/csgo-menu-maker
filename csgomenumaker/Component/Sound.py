from .. import Menu

from .ConfigType import ConfigType


@ConfigType("sound.master")
class Master(Menu.Bar):
    defaultName = "Master Volume"
    defaultDesc = "Change the game's master volume."

    def __init__(self, parent, options):
        Menu.Bar.__init__(self, parent, options)
        self.setMin(0)
        self.setMax(1)
        self.setDefault(self.optValue(options, "default", 1.0))
        self.setSteps(self.optValue(options, "steps", 10))
        self.setVar("volume")
        self.makeChoices()


@ConfigType("sound.voice")
class Voice(Menu.Bar):
    defaultName = "Voice Volume"
    defaultDesc = "Change the volume that voice chat should be played at."

    def __init__(self, parent, options):
        Menu.Bar.__init__(self, parent, options)
        self.setMin(0)
        self.setMax(1)
        self.setDefault(self.optValue(options, "default", 1.0))
        self.setSteps(self.optValue(options, "steps", 10))
        self.setVar("voice_scale")
        self.makeChoices()
