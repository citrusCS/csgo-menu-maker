from ..param import *

from .component import *

from . import generic

name_space(
    "server",
    name="Server",
    description="Miscellaneous server commands."
)

@Component(
    "bhopenable",
    "bhop",
    "bunnyhopenable",
    "bunny_hop_enable",
    "allowbunnyhopping",
    "allow_bunny_hopping"
)
class BHopEnable(generic.Choice):
    params = ParamObj(
        Name("BHop Enable"),
        Desc("Enable bunny hopping."),
        Override(
            "choices",
            [
                {
                    "name" : "Off",
                    "commands" : [
                        "sv_enablebunnyhopping 0"
                        "sv_autobunnyhopping 0"
                    ]
                },
                {
                    "name" : "Easy",
                    "commands" : [
                        "sv_enablebunnyhopping 1"
                        "sv_autobunnyhopping 1"
                    ]
                },
                {
                    "name" : "Pro",
                    "commands" : [
                        "sv_enablebunnyhopping 1"
                        "sv_autobunnyhopping 0"
                    ]
                }
            ]
        )
    )

@Component("surfenable", "surf", "surf_enable")
class SurfEnable(generic.Choice):
    params = ParamObj(
        Name("Surf Enable"),
        Desc("Enable and change surf difficulty."),
        Override(
            "choices",
            [
                {
                    "name" : "Off",
                    "commands" : [
                        "sv_accelerate 5.6",
                        "sv_airaccelerate 12"
                    ]
                },
                {
                    "name" : "Very Easy",
                    "commands" : [
                        "sv_accelerate 10",
                        "sv_airaccelerate 1000"
                    ]
                },
                {
                    "name" : "Fun",
                    "commands" : [
                        "sv_accelerate 10",
                        "sv_airaccelerate 800"
                    ]
                },
                {
                    "name" : "Easy",
                    "commands" : [
                        "sv_accelerate 10",
                        "sv_airaccelerate 400"
                    ]
                },
                {
                    "name" : "Medium",
                    "commands" : [
                        "sv_accelerate 10",
                        "sv_airaccelerate 200"
                    ]
                },
                {
                    "name" : "Hard",
                    "commands" : [
                        "sv_accelerate 10",
                        "sv_airaccelerate 150"
                    ]
                },
                {
                    "name" : "Expert",
                    "commands" : [
                        "sv_accelerate 10",
                        "sv_airaccelerate 100"
                    ]
                }
            ]
        ),
        notes=["`sv_airaccelerate` values taken from https://bit.ly/2HaLlPL"]
    )

@Component("coachingenable", "coaching_enable", "coaching")
class CoachingEnable(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Coaching Enable"),
        Desc("Toggle spectators talking to players."),
        Override("convar", "sv_coaching_enabled")
    )

@Component("deadtalkenable", "dead_talk_enable", "deadtalk")
class DeadTalkEnable(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Dead Talk Enable"),
        Desc("Toggle dead players being able to talk to alive players."),
        Override("convar", "sv_deadtalk")
    )

@Component(
    "falldamagescale",
    "fall_damage_scale",
    "falldamage",
    "fall_damage",
    "falldmg",
    "fall_dmg"
)
class FallDamageScale(generic.Bar):
    params = ParamObj(
        Name("Fall Damage Scale"),
        Desc("Change the fall damage multiplier."),
        Override("min", 0),
        Override("max", 2),
        Override("steps", 20),
        Override("convar", "sv_falldamage_scale"),
        Override("style", "percent"),
        Override("default", 1)
    )

@Component(
    "outofammoindicator",
    "out_of_ammo_indicator",
    "noammoindicator",
    "no_ammo_indicator",
    "nai",
    "ooai"
)
class OutOfAmmoIndicator(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("No Ammo Indicator"),
        Desc("Toggle the no-ammo sound."),
        Override("convar", "sv_outofammo_indicator")
    )

name_space()