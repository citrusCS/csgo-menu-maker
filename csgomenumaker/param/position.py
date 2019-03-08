from .sequence import Sequence


class Position(Sequence):
    """
    Subclass of Sequence that accepts three scalar values.
    
    Used for positions and angles.
    """
    def __init__(self, key, *args, **kwargs):
        Sequence.__init__(
            self, 
            key, 
            *args, 
            **kwargs, 
            seqtypes=(int, float), 
            seqlen=3,
            number=True
        )
