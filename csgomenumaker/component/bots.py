from ..param import *

from .component import *

from . import generic

name_space(
    "bots",
    name="Bots",
    description=
        "Bot related commands which do things like add bots, change bot"
        " difficulty, etc."
)

@Component("addct", "add_ct")
class AddCT(generic.FireableCmd):
    params = ParamObj(
        Name("Add CT"),
        Desc("Add a bot to the Counter-Terrorist team."),
        Override("concmd", "bot_add_ct")
    )

@Component("addt", "add_t")
class AddT(generic.FireableCmd):
    params = ParamObj(
        Name("Add T"),
        Desc("Add a bot to the Terrorist team."),
        Override("concmd", "bot_add_t")
    )

@Component("kick")
class Kick(generic.FireableCmd):
    params = ParamObj(
        Name("Kick All"),
        Desc("Kick all bots."),
        Override("concmd", "bot_kick")
    )

@Component("kill")
class Kill(generic.FireableCmd):
    params = ParamObj(
        Name("Kill All"),
        Desc("Kill all bots, regardless of team"),
        Override("concmd", "bot_kill"),
        flags=["cheat"]
    )

@Component("kill.ct", "kill_ct")
class KillCT(generic.FireableCmd):
    params = ParamObj(
        Name("Kill CT"),
        Desc("Kill all Counter-Terrorist bots."),
        Override("concmd", "bot_kill ct"),
        flags=["cheat"]
    )

@Component("kill.t", "kill_t")
class KillT(generic.FireableCmd):
    params = ParamObj(
        Name("Kill T"),
        Desc("Kill all Terrorist bots."),
        Override("concmd", "bot_kill t"),
        flags=["cheat"]
    )

@Component("stop")
class Stop(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Stop"),
        Desc("Stop all bot processing."),
        Override("convar", "bot_stop"),
        flags=["cheat"]
    )

@Component("allweapons", "all_weapons")
class AllWeapons(generic.FireableCmd):
    params = ParamObj(
        Name("Allow All Weapons"),
        Desc("Allow bots to use all weapons available."),
        Override("concmd", "bot_all_weapons")
    )

@Component("allowrogues", "allow_rogues", "rogues")
class AllowRogues(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Rogues"),
        Desc(
            "Allow bots to go 'rogue', i.e. stop listening to other team"
            " members."
        ),
        Override("convar", "bot_allow_rogues")
    )

@Component("chatter")
class Chatter(generic.ChoiceVar):
    params = ParamObj(
        Name("Chatter Level"),
        Desc("Control how bots talk."),
        Override("convar", "bot_chatter"),
        Override(
            "choices", 
            [
                "off",
                "radio",
                "minimal",
                "normal"
            ]
        )
    )

@Component("difficulty")
class Difficulty(generic.Bar):
    params = ParamObj(
        Name("Difficulty Level"),
        Desc("Change the skill level of bots."),
        Override("min", 0),
        Override("max", 3),
        Override("steps", 3),
        Override("convar", "bot_difficulty"),
        Override("style", "percent"),
        Override("default", 1)
    )

@Component("dontshoot", "dont_shoot", "noshoot")
class DontShoot(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Don't Shoot"),
        Desc("Toggle whether bots will shoot or not."),
        Override("convar", "bot_dont_shoot"),
        flags=["cheat"]
    )

@Component("freeze")
class Freeze(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Freeze"),
        Desc("Toggle the freezing of bots."),
        Override("convar", "bot_freeze"),
        flags=["cheat"]
    )

name_space(
    "weapon_type",
    name="Weapon Types",
    description="Control which weapons bots are allowed to use."
)

@Component("grenades", "nades")
class Grenades(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Grenades"),
        Desc("Toggle the ability for bots to use grenades."),
        Override("convar", "bot_allow_grenades"),
        Override("default", 1)
    )

@Component("machineguns", "machine_guns")
class MachineGuns(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Machine Guns"),
        Desc("Toggle the ability for bots to use machine guns."),
        Override("convar", "bot_allow_machine_guns"),
        Override("default", 1)
    )

@Component("pistols")
class Pistols(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Pistols"),
        Desc("Toggle the ability for bots to use pistols."),
        Override("convar", "bot_allow_pistols"),
        Override("default", 1)
    )

@Component("rifles")
class Rifles(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Rifles"),
        Desc("Toggle the ability for bots to use rifles."),
        Override("convar", "bot_allow_rifles"),
        Override("default", 1)
    )

@Component("shotguns")
class Shotguns(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Shotguns"),
        Desc("Toggle the ability for bots to use shotguns."),
        Override("convar", "bot_allow_shotguns"),
        Override("default", 1)
    )

@Component("snipers")
class Snipers(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow Snipers"),
        Desc("Toggle the ability for bots to use snipers."),
        Override("convar", "bot_allow_snipers"),
        Override("default", 1)
    )

@Component("submachineguns", "sub_machine_guns", "smgs")
class SubMachineGuns(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Allow SMGS"),
        Desc("Toggle the ability for bots to use sub-machine guns"),
        Override("convar", "bot_allow_sub_machine_guns"),
        Override("default", 1)
    )

name_space()

@Component("quota")
class Quota(generic.Bar):
    params = ParamObj(
        Name("Quota"),
        Desc("Change the amount of usable bots."),
        Override("min", 0),
        Override("max", 32),
        Override("steps", 32),
        Override("convar", "bot_quota"),
        Override("style", "int"),
        Override("default", 10)
    )

@Component("mimic")
class Mimic(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Mimic"),
        Desc("Toggle bot mimicking, allowing bots to mimic your every move."),
        Override("convar", "bot_mimic"),
        flags=["cheat"]
    )

@Component("zombie")
class Zombie(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Zombie"),
        Desc("Toggle bot idle mode, meaning they won't attack when on."),
        Override("convar", "bot_zombie"),
        flags=["cheat"]
    )

@Component("ignoreplayers", "ignore_players")
class IgnorePlayers(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Ignore Players"),
        Desc("Toggle bots ignoring players when determining shooting."),
        Override("convar", "bot_ignore_players"),
        flags=["cheat"]
    )

@Component("jointeam", "join_team")
class JoinTeam(generic.ChoiceVar):
    params = ParamObj(
        Name("Join Team"),
        Desc("Control which team bots will join into."),
        Override("convar", "bot_join_team"),
        Override("choices",
            [
                "any",
                "T",
                "CT"
            ]
        )
    )

@Component("randombuy", "random_buy")
class RandomBuy(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Random Buy"),
        Desc("Toggle bots choosing buys randomly."),
        Override("convar", "bot_randombuy"),
        flags=["cheat"]
    )

@Component("place")
class Place(generic.FireableCmd):
    params = ParamObj(
        Name("Place"),
        Desc("Teleport a bot directly to you."),
        Override("concmd", "bot_place"),
        flags=["cheat"]
    )

name_space()