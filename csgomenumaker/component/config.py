from .. import command
from .. import menu
from ..param import *

from .component import *
from . import generic

name_space(
    "config",
    name="Configuration",
    description=
        "Common configuration options that CS:GO players tend to use the most."
)

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


@Component("crosshair", "crosshairs", "xhair", "xhairs")
class Crosshair(generic.PresetChooser):
    params = ParamObj(
        Name("Crosshair"),
        Desc("Choose from crosshair presets.")
    )

    def __init__(self, parent, options):
        self.preset_type = "crosshair"
        # https://developer.valvesoftware.com/wiki/List_of_CS:GO_Cvars
        generic.PresetChooser.__init__(self, parent, options, 
            ParamObj(
                Binary(
                    "drawoutline",
                    default=1,
                    description=
                        "Draws a black outline around the crosshair for "
                        "better visibility.",
                    convar="cl_crosshair_drawoutline",
                ),
                Number(
                    "dynamic_maxdist_splitratio",
                    min=0,
                    max=1,
                    default=0.35,
                    description=
                        "If using cl_crosshairstyle 2, this is the ratio used "
                        "to determine how long the inner and outer xhair pips "
                        "will be.",
                    convar="cl_crosshair_dynamic_maxdist_splitratio"
                ),
                Number(
                    "dynamic_splitalpha_innermod",
                    min=0,
                    max=1,
                    default=0.5,
                    description=
                        "If using cl_crosshairstyle 2, this is the alpha "
                        "modification that will be used for the INNER "
                        "crosshair pips once they've split.",
                    convar="cl_crosshair_dynamic_splitalpha_innermod"
                ),
                Number(
                    "dynamic_splitalpha_outermod",
                    min=0.3,
                    max=1,
                    default=0.5,
                    description=
                        "If using cl_crosshairstyle 2, this is the alpha "
                        "modification that will be used for the OUTER "
                        "crosshair pips once they've split.",
                    convar="cl_crosshair_dynamic_splitalpha_outermod"
                ),
                Number(
                    "dynamic_splitdist",
                    default=7,
                    description=
                        "If using cl_crosshairstyle 2, this is the distance "
                        "that the crosshair pips will split into 2.",
                    convar="cl_crosshair_dynamic_splitdist"
                ),
                Number(
                    "outline_thickness",
                    min=0.1,
                    max=3,
                    default=1,
                    description=
                        "Set how thick you want your crosshair outline to "
                        "draw.",
                    convar="cl_crosshair_outlinethickness"
                ),
                # Number(
                    # "recoil",
                    # min=0,
                    # max=1,
                    # default=0,
                    # hide=True,
                    # cheat=True,
                    # description=
                        # "Recoil/aimpunch will move the user's crosshair to "
                        # "show the effect.",
                    # convar="cl_crosshair_recoil"
                # ),
                Binary(
                    "sniper_show_normal_inaccuracy",
                    default=0,
                    description=
                        "Include standing inaccuracy when determining sniper "
                        "crosshair blur.",
                    convar="cl_crosshair_sniper_show_normal_inaccuracy"
                ),
                Number(
                    "sniper_width",
                    default=1,
                    description=
                        "If >1 sniper scope cross lines gain extra width (1 "
                        "for single-pixel hairline)",
                    convar="cl_crosshair_sniper_width"
                ),
                Binary(
                    "t_shape",
                    default=0,
                    description=
                        "T style crosshair.",
                    convar="cl_crosshair_t"
                ),
                Number(
                    "alpha",
                    min=0,
                    max=255,
                    default=200,
                    description="Crosshair transparency.",
                    convar="cl_crosshairalpha"
                ),
                Color(
                    "color",
                    default=[50, 250, 50],
                    description="Crosshair RGB color.",
                    convar=[
                        "cl_crosshaircolor_r",
                        "cl_crosshaircolor_g",
                        "cl_crosshaircolor_b"
                    ]
                ),
                Binary(
                    "dot",
                    default=1,
                    description=
                        "Show dot in the middle of the crosshair.",
                    convar="cl_crosshairdot"
                ),
                Number(
                    "gap",
                    default=1,
                    description="Crosshair gap size.",
                    convar="cl_crosshairgap"
                ),
                Binary(
                    "gap_useweaponvalue",
                    default=0,
                    description=
                        "If set to 1, the gap will update dynamically "
                        "based on which weapon is currently equipped ",
                    convar="cl_crosshairgap_useweaponvalue"
                ),
                Number(
                    "fixed_gap",
                    default=3,
                    description=
                        "How big to make the gap between the pips in the "
                        "fixed crosshair",
                    convar="cl_fixedcrosshairgap"
                ),
                Number(
                    "size",
                    default=5,
                    description="Crosshair pip size.",
                    convar="cl_crosshairsize"
                ),
                Number(
                    "style",
                    default=5,
                    description=
    "| Number | Name            | Description                             |\n"
    "|--------|-----------------|-----------------------------------------|\n"
    "| 0      | Default         | New look, move/shoot spread             |\n"
    "| 1      | Default Static  | New look, no spread                     |\n"
    "| 2      | Classic         | Old look, eight pips, move/shoot spread |\n"
    "| 3      | Classic Dynamic | Old look, four pips, move/shoot spread  |\n"
    "| 4      | Classic Static  | Old look, four pips, no spread          |\n"
    "| 5      | Classic Legacy  | Old look, four pips, shoot spread       |\n",
                    convar="cl_crosshairstyle"
                ),
                Number(
                    "thickness",
                    default=0.5,
                    description="Crosshair thickness.",
                    convar="cl_crosshairthickness"
                ),
                Binary(
                    "usealpha",
                    default=1,
                    description=
                        "Whether or not to use the alpha value from 'alpha'.",
                    convar="cl_crosshairusealpha"
                ),
                Number(
                    "color_preset",
                    default=5,
                    description=
                        "When 'style' is 0 or 1, this controls the "
                        "crosshair's color.",
                    convar="cl_crosshaircolor"
                ),
                pure=True,
                description="The crosshair to be used."
            )
        )

    def get_commands(self, xhair):
        commands = [
            self.make_param_cmd(xhair, "drawoutline"),
            self.make_param_cmd(xhair, "dynamic_maxdist_splitratio"),
            self.make_param_cmd(xhair, "dynamic_splitalpha_innermod"),
            self.make_param_cmd(xhair, "dynamic_splitalpha_outermod"),
            self.make_param_cmd(xhair, "dynamic_splitdist"),
            self.make_param_cmd(xhair, "outline_thickness"),
            self.make_param_cmd(xhair, "sniper_show_normal_inaccuracy"),
            self.make_param_cmd(xhair, "sniper_width"),
            self.make_param_cmd(xhair, "t_shape"),
            self.make_param_cmd(xhair, "alpha"),
            self.make_param_cmd(xhair, "dot"),
            self.make_param_cmd(xhair, "gap"),
            self.make_param_cmd(xhair, "gap_useweaponvalue"),
            self.make_param_cmd(xhair, "fixed_gap"),
            self.make_param_cmd(xhair, "size"),
            self.make_param_cmd(xhair, "thickness"),
            self.make_param_cmd(xhair, "usealpha"),
            self.make_param_cmd(xhair, "color_preset"),
            self.make_param_cmd(xhair, "style")
        ]
        commands.extend(self.make_param_cmd(xhair, "color"))
        return commands


@Component("viewmodel", "viewmodels", "view_model", "view_models")
class Viewmodel(generic.PresetChooser):
    params = ParamObj(
        Name("Viewmodel"),
        Desc("Choose from viewmodel presets.")
    )
    def __init__(self, parent, options):
        self.preset_type = "viewmodel"
        generic.PresetChooser.__init__(self, parent, options,
            ParamObj(
                Number(
                    "bob_lower",
                    min=5,
                    max=30,
                    default=21,
                    description=
                        "The amount the viewmodel lowers when running.",
                    convar="cl_bob_lower_amt"
                ),
                Number(
                    "bob_lat",
                    min=0.1,
                    max=2,
                    default=0.4,
                    description=
                        "The amount the viewmodel moves side to side when "
                        "running.",
                    convar="cl_bobamt_lat"
                ),
                Number(
                    "bob_vert",
                    min=0.1,
                    max=2,
                    default=0.25,
                    description=
                        "The amount the viewmodel moves up and down when "
                        "running.",
                    convar="cl_bobamt_vert"
                ),
                Number(
                    "bob_cycle",
                    min=0.1,
                    max=2,
                    default=0.98,
                    description="The frequency at which the viewmodel bobs.",
                    convar="cl_bobcycle"
                ),
                Binary(
                    "right_hand",
                    default=1,
                    description="Whether to use the right or left hand.",
                    convar="cl_righthand"
                ),
                Number(
                    "shift_left",
                    min=0.5,
                    max=2,
                    default=1.5,
                    description=
                        "The amount the viewmodel shifts to the left when "
                        "shooting accuracy increases.",
                    convar="cl_viewmodel_shift_left_amt"
                ),
                Number(
                    "shift_right",
                    min=0.25,
                    max=2,
                    default=0.75,
                    description=
                        "The amount the viewmodel shifts to the right when "
                        "shooting accuracy decreases.",
                    convar="cl_viewmodel_shift_right_amt"
                ),
                Number(
                    "fov",
                    default=54,
                    description="The viewmodel's rendered FOV.",
                    convar="viewmodel_fov"
                ),
                Position(
                    "offset",
                    default=[0,0,0],
                    description="The X,Y,Z offset of the rendered viewmodel.",
                    convar=[
                        "viewmodel_offset_x",
                        "viewmodel_offset_y",
                        "viewmodel_offset_z"
                    ]
                ),
                Number(
                    "recoil",
                    min=0,
                    max=1,
                    default=0,
                    description=
                        "Amount of weapon recoil/aimpunch to display on "
                        "viewmodel",
                    convar="viewmodel_recoil"
                ),
                pure=True,
                description="The viewmodel to be used."
            )
        )
    def get_commands(self, vmodel):
        commands = [
            self.make_param_cmd(vmodel, "bob_lower"),
            self.make_param_cmd(vmodel, "bob_lat"),
            self.make_param_cmd(vmodel, "bob_vert"),
            self.make_param_cmd(vmodel, "bob_cycle"),
            self.make_param_cmd(vmodel, "right_hand"),
            self.make_param_cmd(vmodel, "shift_left"),
            self.make_param_cmd(vmodel, "shift_right"),
            self.make_param_cmd(vmodel, "fov"),
            self.make_param_cmd(vmodel, "recoil"),
        ]
        commands.extend(self.make_param_cmd(vmodel, "offset"))
        return commands


@Component("hud", "huds")
class HUD(generic.PresetChooser):
    params = ParamObj(
        Name("HUD"),
        Desc("Choose from HUD presets.")
    )

    def __init__(self, parent, options):
        self.preset_type = "hud"
        generic.PresetChooser.__init__(self, parent, options,
            ParamObj(
                Number(
                    "scale",
                    min=0.5,
                    max=0.95,
                    default=0.85,
                    description="Scales hud elements.",
                    convar="hud_scaling"
                ),
                Binary(
                    "bomb_under_radar",
                    default=1,
                    description="Show the bomb icon under the rader element.",
                    convar="cl_hud_bomb_under_radar"
                ),
                Binary(
                    "radar_centered",
                    default=0,
                    description="Should the radar's center be the player?",
                    convar="cl_radar_always_centered"
                ),
                Binary(
                    "radar_rotate",
                    default=1,
                    description="Should the radar rotate or be north-up?",
                    convar="cl_radar_rotate"
                ),
                Number(
                    "radar_icon_scale",
                    min=0.4,
                    max=1.25,
                    default=0.6,
                    description="Sets the minimum icon scale.",
                    convar="cl_radar_icon_scale_min"
                ),
                Number(
                    "radar_scale",
                    min=0.25,
                    max=1,
                    default=0.7,
                    description="Sets the size of the radar.",
                    convar="cl_radar_icon_scale_min"
                ),
                Binary(
                    "healthammo_style",
                    default=0,
                    description=
                        "Whether to use the default or compact HUD layout",
                    convar="cl_hud_healthammo_style"
                ),
                Binary(
                    "playercount_pos",
                    default=0,
                    description=
                        "Whether to render the player count at the top or "
                        "bottom of the screen",
                    convar="cl_hud_playercount_pos"
                ),
                Binary(
                    "playercount_showcount",
                    default=0,
                    description=
                        "Whether to show avatars or player counts at the top "
                        "of the screen",
                    convar="cl_hud_playercount_showcount"
                ),
                Number(
                    "color_preset",
                    min=0,
                    max=12,
                    default=12,
                    description="Which color the HUD should be rendered in.",
                    convar="cl_hud_color"
                ),
                pure=True,
                description="The HUD configuration to be used."
            )
        )

    def get_commands(self, hud):
        commands = [
            self.make_param_cmd(hud, "scale"),
            self.make_param_cmd(hud, "bomb_under_radar"),
            self.make_param_cmd(hud, "radar_centered"),
            self.make_param_cmd(hud, "radar_rotate"),
            self.make_param_cmd(hud, "radar_icon_scale"),
            self.make_param_cmd(hud, "radar_scale"),
            self.make_param_cmd(hud, "healthammo_style"),
            self.make_param_cmd(hud, "playercount_pos"),
            self.make_param_cmd(hud, "playercount_showcount"),
            self.make_param_cmd(hud, "color_preset")
        ]
        return commands


@Component("autobuys", "autobuy", "auto_buys", "auto_buy")
class Autobuys(generic.PresetChooser):
    params = ParamObj(
        Name("Autobuys"),
        Desc("Choose between autobuy presets.")
    )
    
    def __init__(self, parent, options):
        self.preset_type = "autobuys"
        generic.PresetChooser.__init__(self, parent, options,
            ParamObj(
                Flex(
                    "binds",
                    ParamObj(
                        String(
                            "key",
                            description="The key to bind this weapon to.",
                            ex_vals=["o","p","f1","f2","f3"]
                        ),
                        String(
                            "weapon",
                            description="The weapon to use.",
                            ex_vals=["ak47","hegrenade","deagle"]
                        )
                    ),
                    zerook=True,
                    flexkey="weapon",
                    flexkeyname="key",
                    description="The list of autobuys for this preset."
                ),
                description="The autobuy preset to be used.",
                pure=True
            )
        )

    def flex_callback(self, obj, after):
        """
        Looks through inherit.binds and merges them with the new binds.
        """
        if "inherit" in after and after["inherit"] is not None:
            pseti = self.menu_root.get_preset(self.preset_type, after["inherit"])
            for k in pseti:
                if k not in obj:
                    after[k] = pseti[k]
                if k == "binds":
                    for j in pseti["binds"]:
                        mark = False
                        for l in after["binds"]:
                            if l["key"] == j["key"]:
                                mark = True
                        if not mark:
                            after["binds"].append(j)
        if "name" in after and after["name"] is not None:
            self.menu_root.add_preset(self.preset_type, after["name"], after)
        return after

    def get_commands_seq(self, autobuy, idx):
        ps = self.params["presets"]
        psLen = len(self.params["presets"])
        psBack = ps[(idx - 1) % psLen]
        psFwd = ps[(idx + 1) % psLen]
        indir = command.Indirect(self)
        for nb in [psBack, psFwd]:
            for bind in nb["binds"]:
                key = bind["key"]
                command.Primitive(indir, "unbind", key)
        for bind in autobuy["binds"]:
            #print(autobuy)
            #print(bind)
            key = bind["key"]
            wep = bind["weapon"]
            if wep not in AUTOBUY_WEAPONS:
                self.error("Weapon '%s' not found!" % wep)
            command.Primitive(indir, "bind", [key, '"buy %s"' % wep])
        return [indir,]


@Component("mode", "modes", "gamemodes", "game_modes")
class Mode(generic.PresetChooser):
    params = ParamObj(
        Name("Game Modes"),
        Desc("Choose between different user-defined gamemode presets.")
    )
    
    def __init__(self, parent, options):
        self.preset_type = "mode"
        generic.PresetChooser.__init__(self, parent, options,
            ParamObj(
                Flex(
                    "modes",
                    ParamObj(
                        String(
                            "class",
                            description="The class name of the preset used."
                        ),
                        String(
                            "preset_name",
                            description="The preset name of the preset used."
                        )
                    ),
                    zerook=True,
                    flexkey="preset_name",
                    flexkeyname="class",
                    description="The list of preset class/name pairs.",
                    default=[]
                ),
                description="The gamemode preset to be used.",
                pure=True
            )
        )
        
    def flex_callback(self, obj, after):
        """
        Looks through inherit.modes and merges them with the new modes.
        """
        if "inherit" in after and after["inherit"] is not None:
            pseti = self.menu_root.get_preset(self.preset_type, after["inherit"])
            for k in pseti:
                if k not in obj:
                    after[k] = pseti[k]
                if k == "modes":
                    for j in pseti["modes"]:
                        mark = False
                        for l in after["modes"]:
                            if l["class"] == j["class"]:
                                mark = True
                        if not mark:
                            after["modes"].append(j)
        if "name" in after and after["name"] is not None:
            self.menu_root.add_preset(self.preset_type, after["name"], after)
        return after
        
    def get_commands(self, mode):
        commands = []
        for md in mode["modes"]:
            # For error checking
            self.menu_root.get_preset(
                md["class"],
                md["preset_name"]
            )
            commands.extend(
                self.menu_root.get_preset_cmds(
                    md["class"],
                    md["preset_name"]
                )
            )
        return commands

name_space()