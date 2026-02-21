from typing import Self
from ._loader import _ABILITIES, _LOCALS
import re

class Ability:
    def __init__(self, name: str, data: dict):
        self._name = name
        self._data = data
        self._displayName = _LOCALS.get(name, "")
        self._displayDescription = _LOCALS.get(name+"_Description", "")

    @property
    def displayName(self):
        return self._displayName

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    @property
    def displayDescription(self):
        return self._displayDescription

    @classmethod
    def getByName(cls, name: str) -> Self:
        return Ability(name, _ABILITIES[name])

    @classmethod
    def getByDisplayName(cls, display_name: str) -> Self:
        regex = re.compile(r"npc_dota_hero_[A-z_]+:n")
        for key in _LOCALS:
            value = _LOCALS[key]
            if (not regex.match(key)) and display_name == value:
                return Ability(key, _ABILITIES[key])

        raise IndexError(f"{display_name} - incorrect display name")