from .. import Command
from .. import Menu

from .ConfigType import ConfigType

AUTOBUY_WEAPONS = [
    "ak47",         "aug",          "awp",          "bizon",
    "deagle",       "decoy",        "defuser",      "elite",
    "famas",        "fiveseven",    "flashbang",    "g3sg1",
    "galilar",      "glock",        "hegrenade",    "hkp2000",
    "incgrenade",   "m249",         "m4a1",         "mac10",
    "mag7",         "molotov",      "mp7",          "mp9",
    "negev",        "nova",         "p250",         "p90",
    "revolver",     "sawedoff",     "scar20",       "sg556",
    "smokegrenade", "ssg08",        "taser",        "tec9",
    "ump45",        "vest",         "vesthelm",     "xm1014"
]


@ConfigType("game.crosshair")
class Crosshair(Menu.PresetChooser):
    defaultName = "Crosshair"
    defaultDesc = "Choose between different crosshair presets."

    def getCommands(self, chair):
        self.setPresetType("crosshair")
        commands = [
            self.makeCmd(
                "cl_crosshair_drawoutline",
                self.optValue(chair, "drawoutline", 1)
            ),
            self.makeCmd(
                "cl_crosshair_dynamic_maxdist_splitratio",
                self.optValue(chair, "dynamic_maxdist_splitratio", 0.0)
            ),
            self.makeCmd(
                "cl_crosshair_dynamic_splitalpha_innermod",
                self.optValue(chair, "dynamic_splitalpha_innermod", 1.0)
            ),
            self.makeCmd(
                "cl_crosshair_dynamic_splitalpha_outermod",
                self.optValue(chair, "dynamic_splitalpha_outermod", 0.3)
            ),
            self.makeCmd(
                "cl_crosshair_dynamic_splitdist",
                self.optValue(chair, "dynamic_splitdist", 5.0)
            ),
            self.makeCmd(
                "cl_crosshair_outlinethickness",
                self.optValue(chair, "outlinethickness", 1.0)
            ),
            self.makeCmd(
                "cl_crosshair_recoil",
                self.optValue(chair, "recoil", 0.0)
            ),
            self.makeCmd(
                "cl_crosshair_sniper_show_normal_inaccuracy",
                self.optValue(chair, "sniper_show_normal_inaccuracy", 0)
            ),
            self.makeCmd(
                "cl_crosshair_sniper_width",
                self.optValue(chair, "sniper_width", 1)
            ),
            self.makeCmd(
                "cl_crosshair_t",
                self.optValue(chair, "tshape", 0)
            ),
            self.makeCmd(
                "cl_crosshairalpha",
                self.optValue(chair, "alpha", 200)
            ),
            self.makeCmd(
                "cl_crosshaircolor_r",
                self.optValue(
                    self.optValue(chair, "color", [50, 250, 50]),
                    0,
                    50
                )
            ),
            self.makeCmd(
                "cl_crosshaircolor_g",
                self.optValue(
                    self.optValue(chair, "color", [50, 250, 50]),
                    1,
                    250
                )
            ),
            self.makeCmd(
                "cl_crosshaircolor_b",
                self.optValue(
                    self.optValue(chair, "color", [50, 250, 50]),
                    2,
                    50
                )
            ),
            self.makeCmd(
                "cl_crosshairdot",
                self.optValue(chair, "dot", 1)
            ),
            self.makeCmd(
                "cl_crosshairgap",
                self.optValue(chair, "gap", 1.0)
            ),
            self.makeCmd(
                "cl_fixedcrosshairgap",
                self.optValue(chair, "fixedgap", 3.0)
            ),
            self.makeCmd(
                "cl_crosshairgap_useweaponvalue",
                self.optValue(chair, "gap_useweaponvalue", 0)
            ),
            self.makeCmd(
                "cl_crosshairscale",
                self.optValue(chair, "scale", 0.0)
            ),
            self.makeCmd(
                "cl_crosshairsize",
                self.optValue(chair, "size", 5.0)
            ),
            self.makeCmd(
                "cl_crosshairstyle",
                self.optValue(chair, "style", 2)
            ),
            self.makeCmd(
                "cl_crosshairthickness",
                self.optValue(chair, "thickness", 0.5)
            ),
            self.makeCmd(
                "cl_crosshairusealpha",
                self.optValue(chair, "usealpha", 1)
            ),
            self.makeCmd(
                "cl_crosshaircolor",
                5
            ),
        ]
        return commands


@ConfigType("game.viewmodel")
class Viewmodel(Menu.PresetChooser):
    defaultName = "Viewmodel"
    defaultDesc = "Choose between different viewmodel presets."

    def getCommands(self, vmodel):
        self.setPresetType("viewmodel")
        commands = [
            self.makeCmd(
                "cl_bob_lower_amt",
                self.optValue(vmodel, "bob_lower", 21.0)
            ),
            self.makeCmd(
                "cl_bobamt_lat",
                self.optValue(vmodel, "bob_lat", 0.4)
            ),
            self.makeCmd(
                "cl_bobamt_vert",
                self.optValue(vmodel, "bob_vert", 0.25)
            ),
            self.makeCmd(
                "cl_bobcycle",
                self.optValue(vmodel, "bob_cycle", 0.98)
            ),
            self.makeCmd(
                "cl_righthand",
                self.optValue(vmodel, "right_hand", 1)
            ),
            self.makeCmd(
                "cl_viewmodel_shift_left_amt",
                self.optValue(vmodel, "shift_left", 1.5)
            ),
            self.makeCmd(
                "cl_viewmodel_shift_right_amt",
                self.optValue(vmodel, "shift_right", 0.75)
            ),
            self.makeCmd(
                "viewmodel_fov",
                self.optValue(vmodel, "fov", 68.0)
            ),
            self.makeCmd(
                "viewmodel_offset_x",
                self.optValue(vmodel, "offset_x", 2.5)
            ),
            self.makeCmd(
                "viewmodel_offset_y",
                self.optValue(vmodel, "offset_y", 0.0)
            ),
            self.makeCmd(
                "viewmodel_offset_z",
                self.optValue(vmodel, "offset_z", -1.5)
            ),
            self.makeCmd(
                "viewmodel_recoil",
                self.optValue(vmodel, "recoil", 1.0)
            )
        ]
        return commands


@ConfigType("game.hud")
class HUD(Menu.PresetChooser):
    defaultName = "HUD"
    defaultDesc = "Choose between different HUD presets."

    def getCommands(self, hud):
        self.setPresetType("hud")
        commands = [
            self.makeCmd(
                "hud_scaling",
                self.optValue(hud, "scale", 1.0)
            ),
            self.makeCmd(
                "cl_hud_bomb_under_radar",
                self.optValue(hud, "bomb_under_radar", 1.0)
            ),
            self.makeCmd(
                "cl_radar_always_centered",
                self.optValue(hud, "radar_centered", 0.0)
            ),
            self.makeCmd(
                "cl_radar_rotate",
                self.optValue(hud, "radar_rotate", 1.0)
            ),
            self.makeCmd(
                "cl_radar_icon_scale_min",
                self.optValue(hud, "radar_icon_scale", 0.6)
            ),
            self.makeCmd(
                "cl_radar_scale",
                self.optValue(hud, "radar_scale", 0.45)
            ),
            self.makeCmd(
                "cl_hud_healthammo_style",
                self.optValue(hud, "healthammo_style", 0)
            ),
            self.makeCmd(
                "cl_hud_playercount_pos",
                self.optValue(hud, "playercount_pos", 0)
            ),
            self.makeCmd(
                "cl_hud_playercount_showcount",
                self.optValue(hud, "playercount_showcount", 0)
            ),
            self.makeCmd(
                "cl_hud_color",
                self.optValue(hud, "color", 0)
            )
        ]
        return commands


@ConfigType("game.autobuys")
class Autobuys(Menu.PresetChooser):
    defaultName = "Autobuys"
    defaultDesc = "Choose between different autobuy presets."

    def getCommands(self, autobuy):
        self.setPresetType("autobuys")
        self.optTypeKey(autobuy, "binds", list())
        commands = []
        for bind in autobuy["binds"]:
            self.optTypeKey(bind, "key", str())
            key = bind["key"]
            self.optTypeKey(bind, "weapon", str())
            wep = bind["weapon"]
            if wep not in AUTOBUY_WEAPONS:
                self.error("Weapon '%s' not found!" % wep)
            indir = Command.Indirect(self)
            Command.Primitive(indir, "bind", [key, '"buy %s"' % wep])
            commands.append(indir)
        return commands

    def getCommandsExit(self, autobuy):
        self.optTypeKey(autobuy, "binds", list())
        commands = []
        for bind in autobuy["binds"]:
            self.optTypeKey(bind, "key", str())
            commands.append(self.makeCmd("unbind", bind["key"]))
        return commands


@ConfigType("game.mode")
class Mode(Menu.PresetChooser):
    defaultName = "Game Mode"
    defaultDesc = "Choose between different user-defined gamemode presets."

    def getCommands(self, mode):
        psets = self.optValue(mode, "presets", dict())
        commands = []
        for pset in psets.keys():
            comp = self.menuRoot.getPreset(pset, psets[pset])
            commands.append(comp)
        other = self.optValue(mode, "extra", list())
        for cmd in other:
            args = cmd.split(" ")
            if len(args) == 0:
                self.error("Not enough arguments in command '%s'" % cmd)
            concmd, ag = (args[0], args[1:])
            commands.append(CommandPrimitive(self, "", concmd, ag))
        return commands
