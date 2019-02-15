#!/usr/bin/env python3

import argparse
import sys

from . import Component

parser = argparse.ArgumentParser(
    prog="csgomenumaker",
    description="Generate a console menu for CSGO."
)

parser.add_argument(
    "file"
)

args = parser.parse_args(sys.argv[1:])

Component.ConfigLoader(args.file)
