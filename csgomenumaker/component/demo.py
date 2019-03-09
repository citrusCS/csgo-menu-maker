from .. import command
from .. import menu
from ..param import *

from .component import *

from . import generic

name_space(
    "demo",
    name="Demo",
    description="Demo recording, playback, and control."
)


@Component("record")
class Record(menu.SlotChooser):
    params = ParamObj(
        Name("Record"),
        Desc("Record a Demo."),
        Number(
            "slots",
            min=1,
            max=30,
            default=10,
            description="The number of slots to be made."
        )
    )

    def __init__(self, parent, options):
        menu.SlotChooser.__init__(self, parent, options)
        self.verb = "Record to"
        self.slots = self.params["slots"]
        self.make_choices()

    def get_command(self, slot):
        cmd = command.Primitive(
            self,
            "record",
            [self.root.name_space+"_%i.dem" % slot]
        )
        return cmd


@Component("play")
class Play(menu.SlotChooser):
    params = ParamObj(
        Name("Play"),
        Desc("Play a Demo."),
        Number(
            "slots",
            min=1,
            max=30,
            default=10,
            description="The number of slots to be made."
        )
    )

    def __init__(self, parent, options):
        menu.SlotChooser.__init__(self, parent, options)
        self.verb = "Play from"
        self.slots = self.params["slots"]
        self.make_choices()

    def get_command(self, slot):
        cmd = command.Primitive(
            self,
            "playdemo",
            [self.root.name_space+"_%i.dem" % slot]
        )
        return cmd


@Component("stop")
class Stop(generic.FireableCmd):
    params = ParamObj(
        Name("Stop"),
        Desc("Stop playing a demo."),
        Override("concmd", "stopdemo")
    )


@Component("ui")
class UI(generic.FireableCmd):
    params = ParamObj(
        Name("UI"),
        Desc("Open the demo UI."),
        Override("concmd", "demoui")
    )


# 2019/03/03: FINALLY DONE! This is the last file I wrote!

name_space()
