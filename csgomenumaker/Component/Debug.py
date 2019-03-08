from .. import menu
from ..param import *

from .component import *

from . import generic

name_space(
    "debug",
    name="Debug",
    description=
        "Debugging options that show different data on-screen, such as fps,"
        " position, traces, etc."
)

@Component("showpos", "show_pos")
class ShowPos(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show Position"),
        Desc("Show the player's position in the top left of the screen."),
        Override("convar", "cl_showpos")
    )

@Component("showfps", "show_fps")
class ShowFPS(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show FPS"),
        Desc("Show the FPS and map name in the top left of the screen."),
        Override("convar", "cl_showfps")
    )

@Component("netgraph", "net_graph")
class NetGraph(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Net Graph"),
        Desc("Show network stats and frames per second."),
        Override("convar", "net_graph")
    )

@Component("entityreport", "entity_report")
class EntityReport(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Entity Report"),
        Desc("Show a list of all entities in the scene."),
        Override("convar", "cl_entityreport"),
        flags=["cheat"]
    )

@Component("drawwireframe", "draw_wireframe")
class DrawWireframe(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Draw Wireframe"),
        Desc("Draw a wireframe over the scene."),
        Override("convar", "mat_wireframe"),
        flags=["cheat"]
    )

@Component("showevents", "show_events")
class ShowEvents(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show Events"),
        Desc("Show entity event firing info in the top right of the screen."),
        Override("convar", "cl_showevents"),
        flags=["cheat"]
    )

@Component("visualizetraces", "visualize_traces")
class VisualizeTraces(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Visualize Traces"),
        Desc("Show raycast visualizations as lines."),
        Override("convar", "r_visualizetraces"),
        flags=["cheat"]
    )

@Component("showbudget", "show_budget")
class ShowBudget(generic.Choice):
    params = ParamObj(
        Name("Show Render Budget"),
        Desc(
            "Show information about the current render budget, which tracks"
            " the amounts of time each stage of rendering takes."
        ),
        Override(
            "choices",
            [
                {
                    "name" : "-showbudget",
                    "commands" : [
                        "-showbudget"
                    ]
                },
                {
                    "name" : "+showbudget",
                    "commands" : [
                        "+showbudget"
                    ]
                }
            ]
        ),
        flags=["cheat"]
    )

@Component("drawskeleton", "draw_skeleton")
class DrawSkeleton(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Draw Skeletons"),
        Desc("Draw bone entity skeletons in wireframe form."),
        Override("convar", "enable_skeleton_draw"),
        flags=["cheat"]
    )

@Component("debugmenu", "debug_menu")
class DebugMenu(generic.FireableCmd):
    params = ParamObj(
        Name("Debug Menu"),
        Desc("Open/Close the debug menu."),
        Override("concmd", "debugsystemui"),
        flags=["cheat", "needs_fireable"]
    )

@Component("lockpvs", "lock_pvs")
class LockPVS(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Lock PVS"),
        Desc(
            "Lock/Unlock the PVS (Partially Visible Set) of polygons."
        ),
        Override("convar", "r_lockpvs"),
        flags=["cheat"]
    )

@Component(
    "drawvguitree",
    "draw_vgui_tree",
    "vguitree",
    "vgui_tree",
    "vguidrawtree",
    "vgui_draw_tree"
)
class DrawVGUITree(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Draw VGUI Tree"),
        Desc("Draw a tree of all VGUI widgets and their info."),
        Override("convar", "vgui_draw_tree")
    )

@Component("showsound", "show_sound")
class ShowSound(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show Sound"),
        Desc(
            "Show a list of currently playing sounds and their info in the top"
            " right of the screen."
        ),
        Override("convar", "snd_show"),
        flags=["cheat"]
    )

@Component("showlagcompensation", "show_lag_compensation")
class ShowLagCompensation(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show Lag Compensation"),
        Desc("Show a lag compensated hitboxes, clientside."),
        Override("convar", "sv_showlagcompensation")
    )

@Component("showbullethits", "show_bullet_hits")
class ShowBulletHits(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show Bullet Hits"),
        Desc("Show bullet hits as red cylinders when they hit an entity."),
        Override("convar", "sv_showbullethits"),
        flags=["replicated"]
    )

@Component("showimpacts", "show_impacts")
class ShowImpacts(generic.ChoiceVarBinary):
    params = ParamObj(
        Name("Show Impacts"),
        Desc("Show impacts as red/blue boxes wherever the bullet hits."),
        Override("convar", "sv_showimpacts"),
        flags=["replicated"]
    )

name_space()