from .. import Command
from .. import Menu

from .ConfigType import ConfigType


@ConfigType("demo.record")
class Record(Menu.SlotChooser):
    defaultName = "Record Demo"
    defaultDesc = "Record a demo to an available slot."

    def __init__(self, parent, options):
        Menu.SlotChooser.__init__(self, parent, options)
        self.setVerb("Record to")
        self.setSlots(self.optValue(options, "slots", 16))
        self.makeChoices()

    def getCommand(self, slot):
        cmd = Command.Primitive(
            self,
            "record",
            [self.root.nameSpace+"_%i.dem" % slot]
        )
        return cmd


@ConfigType("demo.play")
class Play(Menu.SlotChooser):
    defaultName = "Play Demo"
    defaultDesc = "Play the demo in a selected slot."

    def __init__(self, parent, options):
        Menu.SlotChooser.__init__(self, parent, options)
        self.setVerb("Play from")
        self.setSlots(self.optValue(options, "slots", 16))
        self.makeChoices()

    def getCommand(self, slot):
        cmd = Command.Primitive(
            self,
            "playdemo",
            [self.root.nameSpace+"_%i.dem" % slot]
        )
        return cmd


@ConfigType("demo.stop")
class Stop(Menu.FireableCmd):
    defaultName = "Stop Demo"
    defaultDesc = "Stop recording a demo."
    cmd = "stop"


@ConfigType("demo.ui")
class UI(Menu.FireableCmd):
    defaultName = "Open Demo UI"
    defaultDesc = "Open the demo playback UI."
    cmd = "demoui"
