from .ConfigTypeMapping import *


class ConfigType:
    def __init__(self, typeName):
        self.typeName = typeName

    def __call__(self, cls):
        CONFIG_TYPE_MAPPING[self.typeName] = cls
        return cls
