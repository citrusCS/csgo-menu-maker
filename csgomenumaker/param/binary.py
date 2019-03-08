from .number import Number

class Binary(Number):
    """
    Subclass of Number that only accepts 0 and 1.
    """
    def __init__(self, key, *args, **kwargs):
        Number.__init__(self, key, *args, **kwargs, choices=[0,1])