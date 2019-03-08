from .sequence import Sequence


class Color(Sequence):
    """
    Subclass of Sequence that accepts three integer values between 0 and 255.
    """
    def __init__(self, key, *args, **kwargs):
        Sequence.__init__(
            self, 
            key, 
            *args, 
            **kwargs, 
            seqtypes=(int, float), 
            seqlen=3,
            min=0,
            max=255,
            int=True,
            number=True
        )