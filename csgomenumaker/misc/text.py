import textwrap
import math


def text_center(text, width, padchar=" "):
    """
    Center `text` in a string of width `width` padded on both sides by varying
    lengths of `padchar`.
    """
    tlen = len(text)
    out = ""
    if tlen > width:
        # Append "..." to signify a continuation.
        out = "..."+text[(-1*width)+2:-1]
    elif tlen < width:
        # If we need to pad, add characters to both sides.
        remain = (width-tlen)
        clip1 = math.ceil(remain/2)
        clip2 = remain-clip1
        out = (padchar*clip1)+text+(padchar*clip2)
    return out


def text_extend(text, width, padchar=" "):
    """
    Pad string `text` to width `width` using char `padchar`.
    
    Extend a string 'smartly', that is, don't extend, reduce, if it's already
    too long.
    """
    out = text.ljust(width, padchar)
    if len(out) > width:
        return "..."+out[(-1*width)+2:-1]
    return out


def text_restrict(text, width):
    """
    Restrict string `text` to width `width`.
    """
    if len(text) > width:
        return "..."+text[(-1*width)+2:-1]
    return text


def text_clip_center(text, width):
    """
    Center-clip a string `text` to width `width`. That is, print starting from
    the center, out.
    """
    clip = 0
    if len(text) > width:
        clip = len(text)-width
    clip1 = math.ceil(clip/2)
    clip2 = clip-clip1
    return text[clip1:][:-clip2]


def text_word_wrap(text, width):
    """
    Word-wrap a string to width `width`.
    """
    return textwrap.wrap(text, width)
