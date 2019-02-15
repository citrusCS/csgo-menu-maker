import textwrap
import math


def TextCenter(text, width, padchar=" "):
    tlen = len(text)
    out = ""
    if tlen > width:
        out = "..."+text[(-1*width)+2:-1]
    elif tlen < width:
        remain = (width-tlen)
        clip1 = math.ceil(remain/2)
        clip2 = remain-clip1
        out = (padchar*clip1)+text+(padchar*clip2)
    return out


def TextExtend(text, width, padchar=" "):
    out = text.ljust(width, padchar)
    if len(out) > width:
        return "..."+out[(-1*width)+2:-1]
    return out


def TextRestrict(text, width):
    if len(text) > width:
        return "..."+text[(-1*width)+2:-1]
    return text


def TextClipCenter(text, width):
    clip = 0
    if len(text) > width:
        clip = len(text)-width
    clip1 = math.ceil(clip/2)
    clip2 = clip-clip1
    return text[clip1:][:-clip2]


def TextWordWrap(text, width):
    return textwrap.wrap(text, width)
