from .. import Command
from .. import Menu

from .ConfigType import ConfigType


@ConfigType("cheats.enable")
class Enable(Menu.ChoiceVarBinary):
    defaultName = "Cheats Enable"
    defaultDesc = "Enable/disable cheats."
    var = "sv_cheats"


@ConfigType("cheats.noclip")
class NoclipEnable(Menu.ChoiceVarBinary):
    defaultName = "Noclip Enable"
    defaultDesc = "Enable/disable noclip."
    var = "noclip"


@ConfigType("cheats.god")
class GodToggle(Menu.FireableCmd):
    defaultName = "Godmode Enable"
    defaultDesc = "Toggle godmode."
    cmd = "god"


@ConfigType("cheats.buddha")
class BuddhaEnable(Menu.ChoiceVarBinary):
    defaultName = "Buddha Enable"
    defaultDesc = "Enable/disable buddha mode."
    var = "buddha"


@ConfigType("cheats.notarget")
class NotargetEnable(Menu.ChoiceVarBinary):
    defaultName = "NoTarget Enable"
    defaultDesc = "Enable/disable notarget mode."
    var = "notarget"


@ConfigType("cheats.givecurrentammo")
class GiveCurrentAmmo(Menu.FireableCmd):
    defaultName = "Give Current Ammo"
    defaultDesc = "Give yourself ammo for the weapon in your main hand."
    cmd = "givecurrentammo"


@ConfigType("cheats.giveweapon")
class GiveWeapon(Menu.Fireable):
    defaultName = "Give Weapon"
    defaultDesc = "Give yourself a weapon."

    def __init__(self, parent, options):
        Menu.Fireable.__init__(self, parent, options)
        self.optTypeKey(options, "weapon", str())
        self.setCommand(
            Command.Primitive(
                self,
                "give",
                [
                    "weapon_"+self.options["weapon"]
                ]
            )
        )
        self.setText("give %s" % options["weapon"])
        self.makeChoices()


@ConfigType("cheats.fog")
class FogEnable(Menu.ChoiceVarBinary):
    defaultName = "Fog Enable"
    defaultDesc = "Enable/disable fog."
    var = "fog_enable"
    default = 1


@ConfigType("cheats.norecoil")
class RecoilEnable(Menu.ChoiceVarBinary):
    defaultName = "Recoil Enable"
    defaultDesc = "Enable/disable recoil."
    var = "weapon_accuracy_nospread"


@ConfigType("cheats.wireframe")
class WireframeEnable(Menu.ChoiceVarBinary):
    defaultName = "Wireframe Enable"
    defaultDesc = "Enable/disable wireframe rendering."
    var = "mat_wireframe"


@ConfigType("cheats.drawothermodels")
class DOMEnable(Menu.ChoiceVarBinary):
    defaultName = "Draw Other Models Enable"
    defaultDesc = "Enable/disable rendering of models."
    var = "r_drawothermodels"
    default = 1


@ConfigType("cheats.timescale")
class Timescale(Menu.Bar):
    defaultName = "Timescale Set"
    defaultDesc = "Set the host timescale."

    def __init__(self, parent, options):
        Menu.Bar.__init__(self, parent, options)
        self.setMin(0)
        self.setMax(self.optValue(options, "max", 2.0))
        self.setDefault(self.optValue(options, "default", 1.0))
        self.setSteps(self.optValue(options, "steps", 20))
        self.setVar("host_timescale")
        self.makeChoices()


@ConfigType("cheats.thirdperson")
class ThirdPerson(Menu.Choice):
    defaultName = "Thirdperson Enable"
    defaultDesc = "Enable/disable third person mode."

    def __init__(self, parent, options):
        Menu.Choice.__init__(self, parent, options)
        self.addChoice(
            "firstperson",
            Command.Primitive(
                self,
                "firstperson",
                []
            )
        )
        self.addChoice(
            "thirdperson",
            Command.Primitive(
                self,
                "thirdperson",
                []
            )
        )
        self.makeChoices()
