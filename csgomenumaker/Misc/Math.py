def lerp(min, max, rat):
    """
    Interpolate between `min` and `max` with the 0-1 ratio `rat`.
    """
    return min+(max-min)*rat


def clamp(min, max, val):
    """
    Clamp `val` between `min` and `max`.
    """
    # https://stackoverflow.com/questions/4092528/how-to-clamp-an-integer-to-some-range
    # Absolutely wonderful. OMG.
    sorted((min, val, max))[1]
