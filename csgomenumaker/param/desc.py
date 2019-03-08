from .string import String

class Desc(String):
    """
    Convenience class to generate a description key with only one argument!
    
    Fancy.
    """
    def __init__(self, name):
        String.__init__(
            self, 
            "desc", 
            default=name, 
            description="The component's description.",
            nodoc=True
        )