from .. import Menu

from .ConfigType import ConfigType


@ConfigType("debug.showpos")
class Showpos(Menu.ChoiceVarBinary):
    defaultName = "Show Position"
    defaultDesc = \
        "Show the player's position in the top left corner of the screen."
    var = "cl_showpos"


@ConfigType("debug.showfps")
class FPS(Menu.ChoiceVarBinary):
    defaultName = "Show FPS"
    defaultDesc = "Show the player's FPS in the top left corner of the screen."
    var = "cl_showfps"


@ConfigType("debug.netgraph")
class NetGraph(Menu.ChoiceVarBinary):
    defaultName = "Show Net Graph"
    defaultDesc = "Show the network graph."
    var = "net_graph"


@ConfigType("debug.entityreport")
class EntityReport(Menu.ChoiceVarBinary):
    defaultName = "Show Entity Report"
    defaultDesc = "Show an overview of all entitites in the scene."
    var = "cl_entityreport"
