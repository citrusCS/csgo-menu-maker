from ..param import *

from .component import *

from . import generic


name_space(
    "sound",
    name="Sound",
    description=(
        "Sound and DSP settings, including volume adjustments for various"
        " parts of the game."
    )
)


name_space(
    "volume",
    name="Volume",
    description=(
        "Volume adjustment for the various game contexts, including master,"
        " voice, menu, and others."
    )
)


@Component("master", "volume")
class MasterVolume(generic.Bar):
    params = ParamObj(
        Name("Master Volume"),
        Desc("Change the master volume of the game."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("voice")
class VoiceVolume(generic.Bar):
    params = ParamObj(
        Name("Voice Volume"),
        Desc("Change relative volume of all voice chat."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "voice_scale"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("menu")
class MenuVolume(generic.Bar):
    params = ParamObj(
        Name("Menu Music Volume"),
        Desc("Change relative volume of all menu music."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_menumusic_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("roundstart", "round_start")
class RoundStartVolume(generic.Bar):
    params = ParamObj(
        Name("Round Start Volume"),
        Desc("Change relative volume of all round start messages."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_roundstart_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("roundend", "round_end")
class RoundEndVolume(generic.Bar):
    params = ParamObj(
        Name("Round End Volume"),
        Desc("Change relative volume of all round end messages."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_roundend_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("objective", "bomb_hostage")
class ObjectiveVolume(generic.Bar):
    params = ParamObj(
        Name("Objective Volume"),
        Desc("Change relative volume of all objective messages/sounds."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_mapobjective_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("tensecond", "ten_second", "10second", "10_second")
class TenSecond(generic.Bar):
    params = ParamObj(
        Name("10s Warning Volume"),
        Desc("Change relative volume of all ten-second warnings."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_tensecondwarning_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("deathcam", "death_cam", "deathcamera", "death_camera")
class DeathCam(generic.Bar):
    params = ParamObj(
        Name("Death Camera Volume"),
        Desc("Change relative volume of all death camera music."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_deathcamera_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("mvp", "mostvaluableplayer", "most_valuable_player")
class MVPVolume(generic.Bar):
    params = ParamObj(
        Name("MVP Volume"),
        Desc("Change relative volume of all MVP music."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_mvp_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


@Component("dangerzone", "danger_zone")
class DangerZoneVolume(generic.Bar):
    params = ParamObj(
        Name("Danger Zone Volume"),
        Desc("Change relative volume of all Danger Zone(TM) music."),
        Override("min", 0),
        Override("max", 1),
        Override("steps", 20),
        Override("convar", "snd_dzmusic_volume"),
        Override("style", "percent"),
        Override("default", 1)
    )


name_space()


@Component("reloaddsp", "reload_dsp")
class ReloadDSP(generic.FireableCmd):
    params = ParamObj(
        Name("Reload DSP"),
        Desc("For troubleshooting, reload the DSP."),
        Override("concmd", "dsp_reload"),
        flags=["cheat"]
    )


@Component("reloadsnd", "reload_snd")
class ReloadSND(generic.FireableCmd):
    params = ParamObj(
        Name("Reload Sound"),
        Desc("For troubleshooting, reload the sound system."),
        Override("concmd", "snd_reload"),
        flags=["cheat"]
    )


@Component("gain")
class Gain(generic.FireableCmd):
    params = ParamObj(
        Name("Master Gain"),
        Desc("Adjust gain (multiplier) of volume."),
        Override("concmd", "snd_gain"),
        flags=["cheat"]
    )


name_space()
