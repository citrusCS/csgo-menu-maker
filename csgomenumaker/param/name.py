from .string import String

class Name(String):
    """
    Convenience class to generate a description key with only one argument!
    
    Fancy.
    """
    def __init__(self, name):
        String.__init__(
            self, 
            "name", 
            default=name, 
            description="The component's name.",
            nodoc=True
        )