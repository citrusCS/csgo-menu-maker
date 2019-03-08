from .param import Param


class Override(Param):
    """
    A param type which overrides an inherited param.
    """
    
    def __init__(self, key, value, *args, **kwargs):
        Param.__init__(self, key, *args, **kwargs, nodoc=True)
        self.value = value
    
    def evaluate(self, value):
        """
        Value is set in __init__. No need to do anything.
        """
        pass