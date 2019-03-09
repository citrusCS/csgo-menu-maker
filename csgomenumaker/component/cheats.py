from .. import menu
from ..param import *

from .component import *

from . import generic

name_space(
    "cheats",
    name="Cheats",
    description=(
        "Cheats and cheat options, such as noclip, sv_cheats, god, and others."
    )
)


@Component("enable")
class Enable(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Server Cheats"),
        Desc("Toggle sv_cheats between 0 and 1."),
        Override("convar", "sv_cheats"),
        flags=["cheat"]
    )


@Component("noclip")
class Noclip(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Noclip"),
        Desc("Toggle physics clipping."),
        Override("convar", "noclip"),
        flags=["cheat"]
    )


@Component("noclip.speed", "noclip_speed")
class NoclipSpeed(generic.Bar):
    params = ParamObj(
        Name("Noclip Speed"),
        Desc("Change physics clipping speed."),
        Override("min", 0),
        Override("max", 20),
        Override("steps", 20),
        Override("convar", "sv_noclipspeed"),
        Override("style", "int"),
        Override("default", 5),
        flags=["cheat"]
    )


@Component("god")
class God(generic.FireableCmd):
    params = ParamObj(
        Name("God Mode"),
        Desc("Enable/disable player godmode."),
        Override("concmd", "god"),
        flags=["cheat", "needs_fireable"]
    )


@Component("gods", "teamgod", "team_god")
class Gods(generic.FireableCmd):
    params = ParamObj(
        Name("Gods Mode"),
        Desc("Enable/disable godmode for all players."),
        Override("concmd", "god"),
        flags=["cheat", "needs_fireable"]
    )


@Component("buddha")
class Buddha(generic.FireableCmd):
    params = ParamObj(
        Name("Buddha Mode"),
        Desc("Enable/disable buddha mode for all players."),
        Override("concmd", "buddha"),
        flags=["cheat", "needs_fireable"]
    )


@Component("explode")
class Explode(generic.FireableCmd):
    params = ParamObj(
        Name("Explode"),
        Desc("Explode yourself."),
        Override("concmd", "explode"),
        flags=["cheat"]
    )


@Component("giveammo", "give_ammo", "givecurrentammo", "give_current_ammo")
class GiveAmmo(generic.FireableCmd):
    params = ParamObj(
        Name("Give Ammo"),
        Desc("Give yourself ammo for your currently held weapon."),
        Override("concmd", "givecurrentammo"),
        flags=["cheat"]
    )


@Component("giveweapon", "give_weapon")
class GiveWeapon(menu.FireableCmd):
    params = ParamObj(
        Name("Give Weapon"),
        Desc("Give yourself a weapon."),
        String(
            "weapon",
            description="The weapon to be given."
        ),
        flags=["cheat"]
    )

    def __init__(self, parent, options):
        menu.FireableCmd.__init__(self, parent, options)
        t = "give weapon_"+self.params["weapon"]
        self.set_command(t)
        self.text = t
        self.make_choices()


@Component("fogenable", "fog_enable")
class FogEnable(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Fog Enable"),
        Desc("Toggle fog rendering."),
        Override("convar", "fog_enable"),
        flags=["cheat"]
    )


@Component("recoilscale", "recoil_scale")
class RecoilScale(generic.Bar):
    params = ParamObj(
        Name("Recoil Scale"),
        Desc("Change recoil scale. 0 for no recoil."),
        Override("min", 0),
        Override("max", 10),
        Override("steps", 20),
        Override("convar", "weapon_recoil_scale"),
        Override("style", "int"),
        Override("default", 2),
        flags=["cheat"]
    )


@Component("timescale", "time_scale")
class TimeScale(generic.Bar):
    params = ParamObj(
        Name("Time Scale"),
        Desc("Change the server's time scale. 0 does not make the game stop."),
        Override("min", 0),
        Override("max", 4),
        Override("steps", 20),
        Override("convar", "host_timescale"),
        Override("style", "int"),
        Override("default", 1),
        flags=["cheat"]
    )


@Component("thirdperson", "third_person")
class Thirdperson(generic.Choice):
    params = ParamObj(
        Name("Third Person"),
        Desc("Toggle between third and first person."),
        Override(
            "choices",
            [
                {
                    "name": "firstperson",
                    "commands": [
                        "firstperson"
                    ]
                },
                {
                    "name": "thirdperson",
                    "commands": [
                        "thirdperson"
                    ]
                }
            ]
        ),
        flags=["cheat"]
    )


@Component("grenadetrajectory", "grenade_trajectory")
class GrenadeTrajectory(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Grenade Trajectory"),
        Desc("Toggle the rendering of grenade paths when they are thrown."),
        Override("convar", "sv_grenade_trajectory"),
        flags=["cheat"]
    )


@Component("drawhud", "draw_hud")
class DrawHUD(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Draw HUD"),
        Desc("Toggle the rendering of the HUD."),
        Override("convar", "cl_drawhud"),
        Override("default", 1),
        flags=["cheat"]
    )


@Component("parachute")
class Parachute(generic.FireableCmd):
    params = ParamObj(
        Name("Equip Parachute"),
        Desc("Equip a parachute from DZ maps."),
        Override("concmd", "parachute"),
        flags=["cheat"]
    )


@Component("hurtme", "hurt_me")
class HurtMe(menu.FireableCmd):
    params = ParamObj(
        Name("Hurt Me"),
        Desc("Hurt yourself for a set amount of damage."),
        Number(
            "damage",
            int=True,
            default=10,
            description="The amount of damage that firing this should accrue."
        ),
        flags=["cheat"]
    )

    def __init__(self, parent, options):
        menu.FireableCmd.__init__(self, parent, options)
        t = "hurtme %i" % self.params["damage"]
        self.set_command(t)
        self.text = t
        self.make_choices()


@Component("gravity")
class Gravity(generic.Bar):
    params = ParamObj(
        Name("Gravity"),
        Desc(
            "Change the server's gravity scale, in units per second squared."
        ),
        Override("min", 0),
        Override("max", 1600),
        Override("steps", 16),
        Override("convar", "sv_gravity"),
        Override("style", "int"),
        Override("default", 800),
        flags=["cheat"]
    )


@Component(
    "crosshairrecoil",
    "crosshair_recoil",
    "xhairrecoil",
    "xhair_recoil"
)
class CrosshairRecoil(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Crosshair Recoil"),
        Desc("Toggle the showing of recoil/aimpunch by moving the crosshair."),
        Override("convar", "cl_crosshair_recoil"),
        flags=["cheat"]
    )


@Component("drawviewmodel", "draw_viewmodel")
class DrawViewmodel(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Draw Viewmodel"),
        Desc("Toggle the drawing of the player's viewmodel."),
        Override("convar", "r_drawviewmodel"),
        flags=["cheat"]
    )


name_space()
