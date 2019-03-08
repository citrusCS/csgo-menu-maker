from .. import misc

from ..param import *


class Settings(misc.Loggable):
    """
    Holds settings of the config.
    
    Represents the top-level "settings" key.
    """
    def __init__(self, options):
        self.options = options
        self.params = ParamObj(
            Assoc(
                "keybinds",
                String(
                    "up", 
                    default="uparrow",
                    description="The key used to navigate upwards."
                ),
                String(
                    "down", 
                    default="downarrow",
                    description="The key used to navigate downwards."
                ),
                String(
                    "left", 
                    default="leftarrow",
                    description="The key used to navigate left."
                ),
                String(
                    "right", 
                    default="rightarrow",
                    description="The key used to navigate right."
                ),
                String(
                    "fire", 
                    default="enter",
                    description=
                        "The key used to run a command or enter a folder."
                ),
                String(
                    "back", 
                    default="\\",
                    description="The key used to leave a folder."
                ),
                String(
                    "enable", 
                    default="alt",
                    description="The key used to enable the UI."
                ),
                description="Keys used to interact with the UI."
            ),
            Assoc(
                "sounds",
                String(
                    "updown",
                    default="buttons/button22",
                    description=
                        "The sound played when navigating up or down."
                ),
                String(
                    "leftright",
                    default="ui/menu_accept",
                    description=
                        "The sound played when navigating left or right."
                ),
                String(
                    "forward",
                    default="ui/menu_focus",
                    description=
                        "The sound played when running a command \
                            or entering a folder."
                ),
                String(
                    "backward",
                    default="ui/menu_back",
                    description=
                        "The sound played when leaving a folder."
                ),
                Number(
                    "volume",
                    default=0.8,
                    description=
                        "The volume that menu sounds shall be played at."
                ),
                description="The sounds that will be played on navigation."
            )
        )
        self.params.register(self)
    
    def get_settings(self):
        self.params.evaluate(self.options)
        return self.params.value
        
    def get_error_name(self):
        return "<settings>"
                