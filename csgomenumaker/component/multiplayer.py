from ..param import *

from .component import *

from . import generic

name_space(
    "multiplayer",
    name="Multiplayer",
    description=(
        "Multiplayer options pertaining to how the game is run, such as"
        " friendly fire, buy-anywhere, team managment, etc."
    )
)


@Component("autokick", "auto_kick")
class AutoKick(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Auto Kick"),
        Desc("Toggle kicking idle, team-killing, or team-hurting players."),
        Override("convar", "mp_autokick")
    )


@Component("buyanywhere", "buy_anywhere")
class BuyAnywhere(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Buy Anywhere"),
        Desc("Toggle allowing players to buy weapons anywhere on the map."),
        Override("convar", "mp_buy_anywhere"),
    )


@Component("dropknives", "drop_knives")
class DropKnives(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Drop Knives"),
        Desc("Toggle making players to drop knives on death."),
        Override("convar", "mp_drop_knife_enable")
    )


@Component("friendlyfire", "friendly_fire")
class FriendlyFire(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Friendly Fire"),
        Desc("Toggle allowing friendly fire."),
        Override("convar", "mp_friendlyfire")
    )


@Component("c4enabled", "c4_enabled", "c4enable", "c4_enable")
class C4Enabled(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("C4 Enabled"),
        Desc("Toggle giving Terrorist players C4."),
        Override("convar", "mp_give_player_c4"),
        Override("default", 1)
    )


@Component("randomspawns", "random_spawns", "randomspawn", "random_spawn")
class RandomSpawns(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Random Spawns"),
        Desc("Toggle making players spawn in random locations."),
        Override("convar", "mp_randomspawn")
    )


@Component("restartgame", "restart_game")
class RestartGame(generic.FireableCmd):
    params = ParamObj(
        Name("Restart Game"),
        Desc("Trigger a game restart."),
        Override("concmd", "mp_restartgame")
    )


@Component("forcewin", "force_win")
class ForceWin(generic.FireableCmd):
    params = ParamObj(
        Name("Force Win"),
        Desc("Force your team to win."),
        Override("concmd", "mp_forcewin"),
        flags=["cheat"]
    )


@Component("forcerespawn", "force_respawn")
class ForceRespawn(generic.FireableCmd):
    params = ParamObj(
        Name("Force Respawn"),
        Desc("Force players to respawn."),
        Override("concmd", "mp_forcerespawnplayers"),
        flags=["cheat"]
    )


name_space(
    "teams",
    name="Teams",
    description=(
        "Teams setup and team options, including display options like names,"
        " odds, and flags."
    )
)


@Component("scramble", "scrambeleggs_without_moms_help")
class ScrambleTeams(generic.FireableCmd):
    params = ParamObj(
        Name("Scramble Teams"),
        Desc("Scramble the teams and trigger a game restart."),
        Override("concmd", "mp_scrambleteams")
    )


@Component("swap")
class SwapTeams(generic.FireableCmd):
    params = ParamObj(
        Name("Swap"),
        Desc("Swap the teams and trigger a game restart."),
        Override("concmd", "mp_swapteams")
    )


@Component("switch")
class SwitchTeams(generic.FireableCmd):
    params = ParamObj(
        Name("Switch"),
        Desc("Switch the teams and trigger a game restart."),
        Override("concmd", "mp_switchteams")
    )


@Component("name1preset", "tname_1_preset")
class TeamName1Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("Name 1"),
        Desc("Choose team 1 name presets."),
        Override("convar", "mp_teamname_1")
    )


@Component("name2preset", "name_2_preset")
class TeamName2Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("Name 2"),
        Desc("Choose team 2 name presets."),
        Override("convar", "mp_teamname_2")
    )


@Component("logo1preset", "logo_1_preset")
class Logo1Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("Logo 1"),
        Desc("Choose team 1 logo presets."),
        Override("convar", "mp_teamlogo_1")
    )


@Component("logo2preset", "logo_2_preset")
class TeamLogo2Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("Logo 2"),
        Desc("Choose team 2 logo presets."),
        Override("convar", "mp_teamlogo_2")
    )


@Component("flag1preset", "flag_1_preset")
class TeamFlag1Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("Flag 1"),
        Desc("Choose team 1 flag presets."),
        Override("convar", "mp_teamflag_1")
    )


@Component("flag2preset", "flag_2_preset")
class TeamFlag2Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("Flag 2"),
        Desc("Choose team 2 flag presets."),
        Override("convar", "mp_teamflag_2")
    )


@Component("matchstat1preset", "matchstat_1_preset")
class MatchStat1Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("MatchStat 1"),
        Desc("Choose team 1 matchstat presets."),
        Override("convar", "mp_teammatchstat_1")
    )


@Component("matchstat2preset", "matchstat_2_preset")
class TeamMatchStat2Preset(generic.ChoiceVar):
    params = ParamObj(
        Name("MatchStat 2"),
        Desc("Choose team 2 matchstat presets."),
        Override("convar", "mp_teammatchstat_2")
    )


@Component("odds", "matchodds", "match_odds")
class TeamMatchOdds(generic.Bar):
    params = ParamObj(
        Name("Match Odds"),
        Desc("Change the match odds."),
        Override("min", 0),
        Override("max", 100),
        Override("steps", 50),
        Override("convar", "sv_teamprediction_pct"),
        Override("style", "str"),
        Override("strleft", "CT"),
        Override("strright", "T"),
        Override("default", 50)
    )


name_space()


@Component("tkpunish", "tk_punish")
class TKPunish(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("TK Punish"),
        Desc("Toggle punishing teamkillers/hurters the next round."),
        Override("convar", "mp_tkpunish")
    )


name_space(
    "warmup",
    name="Warmup",
    description="Warmup controls."
)


@Component("start")
class StartWarmup(generic.FireableCmd):
    params = ParamObj(
        Name("Start"),
        Desc("Start the warmup session."),
        Override("concmd", "mp_warmup_start")
    )


@Component("pause")
class PauseWarmup(generic.FireableCmd):
    params = ParamObj(
        Name("Pause"),
        Desc("Pause the warmup session."),
        Override("concmd", "mp_warmup_pause")
    )


@Component("end")
class EndWarmup(generic.FireableCmd):
    params = ParamObj(
        Name("End"),
        Desc("End the warmup session"),
        Override("concmd", "mp_warmup_end")
    )


name_space()


name_space()
